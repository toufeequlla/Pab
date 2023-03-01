import os
import re
import datetime
import time
from behave.model_core import Status
from Common.FileOps import Json
from Common.WebDriver import WebDriver
import shutil
from WebTestCases import config
from ExternalSystems.mail import Mail

browser = None
resultFile = "result.html"
conciseResultFileName = "conciseresult.html"


def before_all(context):
    context.driver = WebDriver()
    context.config.dynamictestdata = {}
    context.config.referencedata = {"scenarioid": 0}
    context.config.imageindex = 0
    for file in os.listdir(config.screenshotpath):
        if file.endswith(".png") or file.endswith("jpg"):
            os.remove(os.path.join(config.screenshotpath, file))

    shutil.copyfile("resultOrig.html", resultFile)
    shutil.copyfile("resultOrig.html", conciseResultFileName)
    with open("result.html", 'at') as f:
        f.write("<h3>Test Results</h3><br><div>Date/Time: " + str(datetime.datetime.now()) +
                "</div><br><br><table id=\"results\"><tr><th>Sl. No.</th><th>scenario Name</th><th>Steps</th><th>Results</th><th>Screenshot</th></tr>")


def before_scenario(context, scenario):
    with open("result.txt", 'at') as f:
        f.write(scenario.name + ": \n")
    with open("result.html", 'at') as f:
        context.config.referencedata["scenarioid"] = context.config.referencedata["scenarioid"] + 1
        f.write("<tr><td>" +
                str(context.config.referencedata["scenarioid"]) + "</td><td>" + scenario.name.split("@")[0] + "</td><td></td><td></td><td></td></tr>")

    context.config.masterdata = Json.read(os.getcwd() + "/WebTestCases/BLC/Res/masterdata.json")
    if os.path.exists(
            os.getcwd() + "/WebTestCases/BLC/Res/" + context.feature.name.strip().lower().replace(" ", "_")+ "_"+config.env + ".json"):
        try:
            context.config.userdata = Json.read(
                os.getcwd() + "/WebTestCases/BLC/Res/" + context.feature.name.strip().lower().replace(" ",
                                                                                                      "_") + "_"+config.env + ".json")
            print("context loaded")
        except:
            print(
                "empty json : " + os.getcwd() + "/WebTestCases/BLC/Res/" + context.feature.name.strip().lower().replace(
                    " ", "_") + ".json")


def before_step(context, step):
    with open("steps.txt", 'at') as f:
        f.write(step.name + "\n")
    if "<dynamic>" in step.name:
        try:
            currtime = datetime.datetime.now().strftime("%d%m%y%H%M%S")
            attribute = re.search("'([a-zA-Z0-9]+)<dynamic>'", step.name).group()
            if attribute not in context.config.dynamictestdata.keys():
                context.config.dynamictestdata[attribute] = attribute.replace("<dynamic>", currtime)
                print("dynamictestdata : " + context.config.dynamictestdata[attribute])
        except Exception as e:
            print(e)


def after_step(context, step):
    if re.search("'([a-zA-Z0-9]+)<dynamic>'", step.name) is not None:
        attribute = re.search("'([a-zA-Z0-9]+)<dynamic>'", step.name).group()
        stepname = step.name.replace(attribute, context.config.dynamictestdata[attribute])
    else:
        stepname = step.name
    with open("result.txt", 'at') as f:
        f.write(stepname + ":\t" + str(step.status) + "\n")
    if not step.name.lower().startswith("wait"):
        with open("result.html", 'at') as f:
            if step.status == Status.passed:
                f.write("<tr><td></td><td></td><td>" + stepname + "</td><td style=\"color:green;\">" +
                        str(step.status).split(".")[1].upper() + "</td><td></td></tr>")
            if step.status == Status.failed:
                f.write("<tr><td></td><td></td><td>" + stepname + "</td><td style=\"color:red;\">" +
                        str(step.status).split(".")[1].upper() + "</td><td><img src=\"cid:"+str(context.config.imageindex)+"\"/></td></tr>")
                context.driver.takeScreenshot(str(context.config.imageindex) + ".png")
                context.config.imageindex += 1


def after_all(context):
    context.driver.driver.close()
    with open("result.html", 'at') as f:
        f.write("</table></body></html>")
  #  Mail.send("result.html", config.screenshotpath)
    print("Done")


def after_scenario(context, scenario):
    with open("result.txt", 'at') as f:
        f.write("\n" + scenario.name + ":" + str(scenario.status) + "\n\n")
    with open("resultconcise.html", 'at') as f:
        if scenario.status == Status.passed:
            f.write("<tr><td>" + str(context.config.referencedata[
                                         "scenarioid"]) + "</td><td>" + scenario.name + "</td><td></td><td style=\"color:green;\">" +
                    str(scenario.status).split(".")[1].upper() + "</td></tr>")
        if scenario.status == Status.failed:
            f.write("<tr><td>" + str(context.config.referencedata[
                                         "scenarioid"]) + "</td><td>" + scenario.name + "</td><td></td><td style=\"color:red;\">" +
                    str(scenario.status).split(".")[1].upper() + "</td></tr>")
