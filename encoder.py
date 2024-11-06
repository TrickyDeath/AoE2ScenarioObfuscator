import random
import time
from hashlib import md5

from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario


def comfound_triggers(scenario: AoE2DEScenario, confound_count, author, type, value=""):
    trigger_manager = scenario.trigger_manager
    # 修改原触发器名与描述
    for trigger in trigger_manager.triggers:
        if type == 0:
            randstr = str(random.Random()) + str(time.time()) + str(trigger)
            trigger.name = md5(randstr.encode("utf-8")).hexdigest()
        elif type == 1:
            trigger.name = value
        # 考虑到触发器任务显示部分功能可能被影响，暂不修改
        # if not (trigger.display_as_objective or trigger.display_on_screen):
        #     trigger.description = "Triggers have been confounded! Copyright reserved by %s" % author
    # 混入空触发器
    for _ in range(confound_count):
        randstr = str(random.Random()) + str(time.time())
        if type == 0:
            randstr = str(random.Random()) + str(time.time()) + str(trigger)
            name = md5(randstr.encode("utf-8")).hexdigest()
        elif type == 1:
            name = value
        trigger = trigger_manager.add_trigger(
            name=name,
            description="Triggers have been confounded! Copyright reserved by %s" % author,
            enabled=False
        )
        trigger.new_condition.timer(timer=10)
    # 打乱顺序
    random.shuffle(trigger_manager.trigger_display_order)


def open_scenario(file_path):
    scenario = AoE2DEScenario.from_file(file_path)
    return scenario


def save_scenario(scenario: AoE2DEScenario, output_file_path):
    scenario.write_to_file(output_file_path)
