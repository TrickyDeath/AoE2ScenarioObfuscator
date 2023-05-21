from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2Scenario
from AoE2ScenarioParser.datasets.trigger_lists import Operation

scenario : AoE2Scenario = AoE2Scenario.from_file("your_scenario")
trigger_mgr = scenario.trigger_manager
trigger = trigger_mgr.add_trigger(
    name="test"
)
trigger.new_effect.change_variable(
    quantity=1,
    operation=Operation.SET,
    variable=1,
    message="variable name"
) 