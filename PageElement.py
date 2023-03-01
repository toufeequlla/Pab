from Common import config

class PageElement:
    @staticmethod
    def get(attribute, feature):
        try:
            name = config.pagefactorymodulepath
            components = name.split('.')
            mod = __import__(components[0])
            for comp in components[1:]:
                mod = getattr(mod, comp)
            mod = getattr(mod, feature.lower())
            mod = getattr(mod, feature)
            m = getattr(mod, attribute)
            return m
        except Exception as e:
            print("Something is not right!!!!" + str(e))
            return None
