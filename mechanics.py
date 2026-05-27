import random
import time


def agent_list(agent_dataset):
    agents = []
    for agent in agent_dataset:
        agents.append(agent)
    return agents

def get_agent_menu(agent_list):
    for i in range (len(agent_list)):
        print(f"{i  + 1}) {agent_list[i]}")

def get_agent(agent_dataset, a_list):
    # agent = random.choice(list(agent_dataset.keys()))
    # agent = agent_choice.lower()
    choice = int(input("\nEnter your agent number: "))
    agent = a_list[choice - 1]
    print(f"\nYou have selected {agent}")
    health = agent_dataset[agent]["Health"]
    damage = agent_dataset[agent]["Damage"]

    return agent, health, damage
 

def get_enemy(enemy_dataset):
    enemy = random.choice(list(enemy_dataset.keys()))
    health = enemy_dataset[enemy]["Health"]
    damage = enemy_dataset[enemy]["Damage"]

    # return enemy, health, damage
    print(f"Your enemy is: {enemy}")
    print(f"Health is {health}")
    print(f"Damage is {damage}\n")

    return enemy, health, damage
    

def attack(agent, agent_health, agent_damage, enemy, enemy_health, enemy_damage):
    while (agent_health and enemy_health) >= 0:
   
        # if (agent_health <= 0) or (enemy_health <= 0):
        #     break
        enemy_health -= agent_damage
        print(f"\n{agent} did {agent_damage} damage to {enemy}, {enemy} health is {enemy_health}")

        agent_health -= enemy_damage
        print(f"{enemy} did {enemy_damage} damage to {agent}, {agent} health is {agent_health}")

        time.sleep(1)
