from agent.deliberative_control.deliberative_control import DeliberativeControl
from agent.prospector_agent import ProspectorAgent
from planner.mdp.mdp_planner import MDPPlanner
from psa import executar as execute
from psa import iniciar as init


def main():

    init("env/amb1.das")

    execute(
        ProspectorAgent(
            DeliberativeControl(
                MDPPlanner()
            )
        )
    )


if __name__ == "__main__":

    main()
