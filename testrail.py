import os
import requests
import json
import base64
import glob
import random
from ExternalSystems import config

PATH = lambda p: os.path.abspath(
    os.path.join(os.path.dirname(__file__), p)
)
'from config import config'


# -----------------------------------------------------------------

class APIClient:
    def __init__(self, base_url):
        self.user = ''
        self.password = ''
        if not base_url.endswith('/'):
            base_url += '/'
        self.__url = base_url + 'index.php?/api/v2/'

    def send_get(self, uri, filepath=None):
        """Issue a GET request (read) against the API.

        Args:
            uri: The API method to call including parameters, e.g. get_case/1.
            filepath: The path and file name for attachment download; used only
                for 'get_attachment/:attachment_id'.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('GET', uri, filepath)

    def send_post(self, uri, data):
        """Issue a POST request (write) against the API.

        Args:
            uri: The API method to call, including parameters, e.g. add_case/1.
            data: The data to submit as part of the request as a dict; strings
                must be UTF-8 encoded. If adding an attachment, must be the
                path to the file.

        Returns:
            A dict containing the result of the request.
        """
        return self.__send_request('POST', uri, data)

    def __send_request(self, method, uri, data):
        url = self.__url + uri

        auth = str(
            base64.b64encode(
                bytes('%s:%s' % (self.user, self.password), 'utf-8')
            ),
            'ascii'
        ).strip()
        headers = {'Authorization': 'Basic ' + auth}

        if method == 'POST':
            if uri[:14] == 'add_attachment':  # add_attachment API method
                files = {'attachment': (open(data, 'rb'))}
                response = requests.post(url, headers=headers, files=files)
                files['attachment'].close()
            else:
                headers['Content-Type'] = 'application/json'
                payload = bytes(json.dumps(data), 'utf-8')
                response = requests.post(url, headers=headers, data=payload)
        else:
            headers['Content-Type'] = 'application/json'
            response = requests.get(url, headers=headers)

        if response.status_code > 201:
            try:
                error = response.json()
            except:  # response.content not formatted as JSON
                error = str(response.content)
            raise APIError('TestRail API returned HTTP %s (%s)' % (response.status_code, error))
        else:
            if uri[:15] == 'get_attachment/':  # Expecting file, not JSON
                try:
                    open(data, 'wb').write(response.content)
                    return (data)
                except:
                    return ("Error saving attachment.")
            else:
                try:
                    return response.json()
                except:  # Nothing to return
                    return {}


class APIError(Exception):
    pass


# -------------------------------------------------------------------


testrail_url = config.testrail_url
testrail_username = config.testrail_username
testrail_password = config.testrail_pwd


def get_testrail_client():
    "Get the TestRail account credentials from the config file"
    # Get the TestRail Url
    client = APIClient(testrail_url)
    # Get and set the TestRail User and Password
    client.user = testrail_username
    client.password = testrail_password
    return client


def update_testrail(case_id, run_id, result_flag, msg=""):
    "Update TestRail for a given run_id and case_id"
    update_flag = False
    # Get the TestRail client account details
    client = get_testrail_client()
    status_id = 1 if result_flag is True else 5

    if run_id is not None:
        try:
            client.send_post(
                'add_result_for_case/%s/%s' % (run_id, case_id), {
                    'status_id': status_id, 'comment': msg})
        except Exception as e:
            print('Exception in update_testrail() updating TestRail.')
            print('PYTHON SAYS: ')
            print(e)
        else:
            print('Updated test result for case: %s in test run: %s with msg:%s' % (case_id, run_id, msg))

    return update_flag


def get_project_id(project_name):
    """Get the project ID using project name"""
    client = get_testrail_client()
    project_id = None
    projects = client.send_get('get_projects')
    for project in projects:
        if project['name'] == project_name:
            project_id = project['id']
            break
    print(project_id)
    return project_id


def get_run_id(test_run_name, project_name):
    """Get the run ID using test name and project name"""
    run_id = None
    client = get_testrail_client()
    project_id = get_project_id(project_name)
    try:
        test_runs = client.send_get('get_runs/%s' % project_id)
    except Exception as e:
        print('Exception in update_testrail() updating TestRail.')
        print('PYTHON SAYS: ')
        print(e)
        return None
    else:
        for test_run in test_runs:
            if test_run['name'] == test_run_name:
                run_id = test_run['id']
                break
        return run_id


def add_run(test_run_name, project_name, suite_id):
    client = get_testrail_client()
    project_id = get_project_id(project_name)

    try:
        result = client.send_post(
            'add_run/%s' % project_id,
            {'suite_id': suite_id, 'name': test_run_name, 'include_all': True, })
        print(result)
        return result
    except Exception as e:
        print('Exception in add_run() updating TestRail.')
        print('PYTHON SAYS: ')
        print(e)


def get_sections(project_ID, suite_ID):
    client = get_testrail_client()
    sections = client.send_get('get_sections/' + project_ID + '&suite_id=' + suite_ID)
    return sections


def get_section(section_ID):
    client = get_testrail_client()
    section = client.send_get('get_section/' + section_ID)
    return section


def create_feature_file(suite_ID, project_ID, run_ID, case_val=0):
    delete_feature_files()
    client = APIClient(testrail_url)
    client.user = testrail_username
    client.password = testrail_password
    cases = client.send_get('get_cases/' + project_ID + '&suite_id=' + suite_ID)
    f = None
    filedata = None
    section_id_2 = 1
    count = 0
    device_no = 1
    val = case_val
    f_phone_number = str(random.randint(4444555500, 4444666600))
    for case in cases:
        if case['custom_autostatus'] != 3:
            section_id_1 = section_id_2
            section_id_2 = case['section_id']
            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print('')
                section_name = str(get_section(str(section_id_2))['name'])
                if "/" or " " in section_name:
                    section_name = section_name.replace("/", "_")
                    section_name = section_name.replace(" ", "_")
                else:
                    pass
                f = open(PATH('../features/' + section_name + '.feature'), "w+")
                tag = str(get_section(str(section_id_2))['name'])
                print(tag)
                tag_name = tag.split('_')
                if count >= case_val:
                    case_val = val + case_val
                    device_no += 1
                    f_phone_number = str(random.randint(4444555500, 4444666600))
                if case_val == 0:
                    filedata = "@" + tag_name[0] + tag_name[1] + '\nFeature: ' + section_name + '\n'
                elif case_val != 0:
                    filedata = "@device" + str(device_no) + '\nFeature: ' + section_name + '\n'
                count += 1
                if case['custom_background'] is not None:
                    filedata += ('\n\nBackground: ' + case['custom_background'].strip())
            if case['title'] is not None:
                if 'happyflow' in str(case['title']):
                    filedata += ('\n\n' + "@" + tag_name[0] + tag_name[1] + '_smoke')
                    if "Scenario:" in str(case['title']):
                        line = ('\n' + case['title'].strip() + ' testrail details_' + str(case['id']) + '_' + run_ID)
                        if "\n" in line:
                            line = line.replace('\n', '')
                            filedata += "\n\n" + line
                        else:
                            filedata += "\n\n" + line
                    else:
                        line = ('\n\nScenario: ' + case['title'].strip() + ' testrail details_' + str(
                            case['id']) + '_' + run_ID)
                        if "\n" in line:
                            line = line.replace('\n', '')
                            filedata += "\n\n" + line
                        else:
                            filedata += "\n\n" + line
                else:
                    if "Scenario:" in str(case['title']):
                        line = ('\n' + case['title'].strip() + ' testrail details_' + str(case['id']) + '_' + run_ID)
                        if "\n" in line:
                            line = line.replace('\n', '')
                            filedata += "\n\n" + line
                        else:
                            filedata += "\n\n" + line
                    else:
                        line = ('\n\nScenario: ' + case['title'].strip() + ' testrail details_' + str(
                            case['id']) + '_' + run_ID)
                        if "\n" in line:
                            line = line.replace('\n', '')
                            filedata += "\n\n" + line
                        else:
                            filedata += "\n\n" + line
            if case['custom_given'] is not None:
                filedata += ('\n\nGiven ' + case['custom_given'].strip())
            if case['custom_when'] is not None:
                filedata += ('\nWhen ' + case['custom_when'].strip())
            if case['custom_then'] is not None:
                filedata += ('\nThen ' + case['custom_then'].strip())
            if case['custom_example'] is not None:
                filedata += ('\n\nExample ' + case['custom_example'].strip())
            filedata = str(filedata).replace('"phone number"', '"' + f_phone_number + '"')
    f.write(filedata)
    f.close()
    print('Number of feature file created = ' + str(count))


def create_feature_from_run(suite_ID, project_ID, run_ID):
    delete_feature_files()
    client = APIClient(testrail_url)
    client.user = testrail_username
    client.password = testrail_password
    suite = client.send_get('get_suite/' + suite_ID)
    feature_name = suite['name'].replace(" ", "_")
    cases = client.send_get('get_tests/' + run_ID)
    f = None
    filedata = None
    section_id_2 = 1
    count = 0
    for case in cases:
        if case['custom_autostatus'] != 3:
            section_id_1 = section_id_2
            section_id_2 = case['section_id']
            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print('')

                f = open(PATH(
                    '../features/' + feature_name + '_' + str(get_section(str(section_id_2))['name']) + '.feature'),
                    "w+")
                filedata = "@" + str(get_section(str(section_id_2))['name']) + '\nFeature: ' + str(
                    get_section(str(section_id_2))['name']) + '\n'
                count += 1
                if case['custom_background'] is not None:
                    filedata += ('\n\nBackground: ' + case['custom_background'].strip())
            if case['title'] is not None:
                filedata += ('\n\n' + case['title'].strip() + ' testrail details_' + str(case['id']) + '_' + run_ID)
            if case['custom_given'] is not None:
                filedata += ('\nGiven ' + case['custom_given'].strip())
            if case['custom_when'] is not None:
                filedata += ('\nWhen ' + case['custom_when'].strip())
            if case['custom_then'] is not None:
                filedata += ('\nThen ' + case['custom_then'].strip())
            if case['custom_example'] is not None:
                filedata += ('\n\nExample ' + case['custom_example'].strip())
    f.write(filedata)
    f.close()
    print('Number of feature file created = ' + str(count))


def create_feature_file_tags(suite_ID, project_ID, run_ID, tag_name=None):
    delete_feature_files()
    client = APIClient(testrail_url)
    client.user = testrail_username
    client.password = testrail_password
    suite = client.send_get('get_suite/' + suite_ID)
    feature_name = suite['name'].replace(" ", "_")
    cases = client.send_get('get_cases/' + project_ID + '&suite_id=' + suite_ID)
    f = None
    filedata = None
    section_id_2 = 1
    count = 0
    tag_names = {"Installation": 1, "Onboarding": 2, "Android": 3, "IOS": 4, "Parity": 5, "Worksheets": 6,
                 "World Map": 7, "Miscellaneous": 8, "Quest Progress": 9, "Chapters/Buildings": 10,
                 "Quests": 11, "Tasks": 12, "Video": 13, "Game": 14,
                 "Interactive Video": 15, "Interstitials": 16, "Sticker Book": 17, "Rewards": 18, "Online": 19,
                 "Offline": 20, "Library": 21, "Parent Zone": 22, "Parent Gating": 23,
                 "Profile Selection": 24, "Profile Picture": 25, "Child Report": 26,
                 "OLAP/Analytics": 27, "Splash Screen": 28, "Transitions": 29, "FTUE": 30, "In-App Rating": 31,
                 "Messaging": 32, "Payments": 33, "Subscription": 34, "Child Profile": 35, "Sessions": 36,
                 "Device": 37, "Progress and Sync": 38,
                 "Network": 39, "Security": 40, "MCQ": 41, "Classify": 42, "Sort": 43, "Hangman": 44,
                 "Match": 45, "Choose": 46, "Count": 47}
    for case in cases:
        flag = False
        if tag_name is None:
            flag = True
        elif tag_names[tag_name] in case['custom_tags']:
            flag = True
        if case['custom_autostatus'] != 3 and flag:
            section_id_1 = section_id_2
            section_id_2 = case['section_id']
            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print('')
                f = open(PATH(
                    '../features/' + feature_name + '_' + str(get_section(str(section_id_2))['name']) + '.feature'),
                    "w+")
                filedata = "@" + str(get_section(str(section_id_2))['name']) + '\nFeature: ' + str(
                    get_section(str(section_id_2))['name']) + '\n'
                count += 1
                if case['custom_background'] is not None:
                    filedata += ('\n\nBackground: ' + case['custom_background'].strip())
            if case['title'] is not None:
                filedata += ('\n\n' + case['title'].strip() + ' testrail details_' + str(case['id']) + '_' + run_ID)
            if case['custom_given'] is not None:
                filedata += ('\nGiven ' + case['custom_given'].strip())
            if case['custom_when'] is not None:
                filedata += ('\nWhen ' + case['custom_when'].strip())
            if case['custom_then'] is not None:
                filedata += ('\nThen ' + case['custom_then'].strip())
            if case['custom_example'] is not None:
                filedata += ('\n\nExample ' + case['custom_example'].strip())
    f.write(filedata)
    f.close()
    print('Number of feature file created = ' + str(count))


def delete_feature_files():
    f_files = glob.glob(PATH('../features/*.feature'))
    for f in f_files:
        os.remove(f)


def get_run(run_id):
    client = get_testrail_client()
    cases = client.send_get('get_case/' + run_id)
    print(cases)
    print(type(cases))
    print('---------------------------------------------------------------------')
    '''
    for i in range(len(cases)):
        print cases[i]
        print '---------------------------------------------------------------------'
    '''


def create_feature_file_of_run(suite_ID, project_ID, run_ID):
    delete_feature_files()
    client = APIClient(testrail_url)
    client.user = testrail_username
    client.password = testrail_password
    cases = client.send_get('get_tests/' + run_ID)
    f = None
    filedata = None
    section_id_2 = 1
    count = 0
    for case in cases:
        if case['custom_autostatus'] != 3:
            case_suite = client.send_get('get_case/' + str(case['case_id']))
            section_id_1 = section_id_2
            section_id_2 = case_suite['section_id']
            if section_id_1 != section_id_2:
                try:
                    f.write(filedata)
                    f.close()
                except:
                    print('')
                print(section_id_2)
                f = open(PATH('../features/' + str(get_section(str(section_id_2))['name']) + '.feature'), "w+")
                tag = str(get_section(str(section_id_2))['name'])
                print(tag)
                tag_name = tag.split('_')
                filedata = "@" + tag_name[0] + tag_name[1] + '\nFeature: ' + str(
                    get_section(str(section_id_2))['name']) + '\n'
                count += 1
                if case['custom_background'] is not None:
                    filedata += ('\n\nBackground: ' + case['custom_background'].strip())
            if case['title'] is not None:
                if 'happyflow' in str(case['title']):
                    filedata += ('\n\n' + "@" + tag_name[0] + tag_name[1] + '_smoke')
                    filedata += ('\n' + case['title'].strip() + ' testrail details_' + str(
                        case_suite['id']) + '_' + run_ID)
                else:
                    filedata += ('\n\n' + case['title'].strip() + ' testrail details_' + str(
                        case_suite['id']) + '_' + run_ID)
            if case['custom_given'] is not None:
                filedata += ('\nGiven ' + case['custom_given'].strip())
            if case['custom_when'] is not None:
                filedata += ('\nWhen ' + case['custom_when'].strip())
            if case['custom_then'] is not None:
                filedata += ('\nThen ' + case['custom_then'].strip())
            if case['custom_example'] is not None:
                filedata += ('\n\nExample ' + case['custom_example'].strip())
    f.write(filedata)
    f.close()
    print('Number of feature file created = ' + str(count))


def update_status(caseid, value):
    client = get_testrail_client()
    client.send_post('update_case/%s' % caseid, {'custom_autostatus': value})


def add_suite(project_name, suite_name):
    client = get_testrail_client()
    pjct_name = project_name
    project_id = get_project_id(pjct_name)
    try:
        result = client.send_post(
            'add_suite/%s' % (project_id),
            {"name": suite_name,
             "description": "This suite is created for testing purpose"})
        print(result)

    except Exception as e:
        print('Exception in add_suite() updating TestRail.')
        print('PYTHON SAYS: ')
        print(e)

    return result['id']


def add_section(project_name, section_name, suite_ID, title):
    client = get_testrail_client()
    pjct_name = project_name
    project_id = get_project_id(pjct_name)
    try:
        result = client.send_post(
            'add_section/%s' % (project_id),
            {
                "suite_id": int(suite_ID),
                "description": str(title),
                "name": section_name
            })

        print(result)
        print(result['id'])

    except Exception as e:
        print('Exception in add_section() updating TestRail.')
        print('PYTHON SAYS: ')
        print(e)

    return result['id']


def add_case(section_id, dict_steps):
    client = get_testrail_client()
    try:
        result = client.send_post(
            'add_case/%s' % (section_id), dict_steps)
        print(result)
    except Exception as e:
        print('Exception in add_section() updating TestRail.')
        print('PYTHON SAYS: ')
        print(e)

    return result['id']