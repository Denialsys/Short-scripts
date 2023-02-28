import os
import re

rule_name_keyword = 'Rule Name:'
sep_keyword = '---'
action_keyword = 'Action:'

firewall_rules = os.popen("netsh advfirewall firewall show rule name=all").read().split("\n")
target_rules = [
    "remote",
    "windows media player",
    "windows peer to peer",
    "windows remote management",
    "network discovery",
    "take a test",
    "file and printer sharing",
    "media center extenders",
    "wireless portable devices",
    "microsoft pay",
    "microsoft people",
    "microsoft store",
    "microsoft photos",
    "microsoft solitaire",
    "wifi direct scan service",
    "wifi direct spooler use",
    "wireless display"]


def create_firewall_modifier():
    """
    Creates a batch file for modifying the firewall and a batch file for
    restoring the modification
    """

    original_rules = []
    target_batch_file_original = 'D:\\Desktop\\firewall original.bat'
    target_batch_file_modifier = 'D:\\Desktop\\firewall modifier.bat'
    cmd = 'netsh advfirewall firewall set rule name="{0}" new action="{1}"\n'

    # Get the rule and its action -----
    json_rule = {}
    for rule in firewall_rules:
        if rule_name_keyword in rule:

            # Check if it is the target rule to modify
            for target_rule in target_rules:
                if target_rule in rule.lower():

                    # Get the rule name
                    stripped_rule = re.sub('  +', '  ', rule).split('  ')
                    current_rule_name = stripped_rule[1]
                    json_rule[stripped_rule[0]] = current_rule_name
                    break

        elif json_rule and action_keyword in rule:

            # Get the action value of the rule
            stripped_rule = re.sub('  +', '  ', rule).split('  ')
            json_rule[stripped_rule[0]] = stripped_rule[1]
            original_rules.append(json_rule)
            json_rule = {}  # Clear the json

    for jsons in original_rules:
        print(jsons)

    # Create a batch file with original action -----
    with open(target_batch_file_original, "w+") as batch_file:
        for rule in original_rules:
            batch_file.write(cmd.format(rule[rule_name_keyword], rule[action_keyword]))

    # Create a batch file with modified action -----
    with open(target_batch_file_modifier, "w+") as batch_file:
        for rule in original_rules:
            batch_file.write(cmd.format(rule[rule_name_keyword], 'Block'))


if __name__ == '__main__':
    create_firewall_modifier()
