'''
import configparser

class ConfigurationParams:
    def __init__(self, config_file , section):
        
        self.config = configparser.ConfigParser(
            comment_prefixes='#',
            inline_comment_prefixes='#'
        )
        self.config.read(config_file)
        self.section = self.config[section]

        for key in self.section:
            config_value = self.section[key]

            if (config_value.isdigit()):
                setattr(self, key, int(config_value))

            elif config_value.replace('.', '', 1).isdigit() and config_value.count('.') < 2:
                setattr(self, key, float(config_value))

            elif '[' in config_value and ']' in config_value:
                setattr(self, key, eval(config_value))

            elif 'time_format' == key:
                setattr(self, key, config_value.replace('_', '%'))

            else:
                setattr(self, key, str(config_value))
                
'''