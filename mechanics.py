import random
import time

'''
Here, 
        a -> agent
        e -> enemy

'''

def agent_list(a_dataset):
    agents = []
    for agent in a_dataset:
        agents.append(agent)
    return agents

def get_agent_menu(a_list):
    for i in range (len(a_list)):
        print(f"{i  + 1}) {a_list[i]}")

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

    # print(f"Your enemy is: {enemy}")
    # print(f"Health is {health}")
    # print(f"Damage is {damage}\n")

    return enemy, health, damage
    

def get_agent_crit(a_dmg):
    
    a_rate = random.uniform(0.1, 0.5)
    a_crit_dmg_rate = random.uniform(1.5, 2.0) # -> incase of floating numbers we use random.uniform
    
    a_normal_dmg = None
    a_normal_dmg = a_dmg
    a_normal_dmg = a_normal_dmg + (a_normal_dmg * a_rate) # -> this is the normal damage, upto the damage agent can normally hit
    

    if a_rate > 0.80:
        a_real_dmg = a_real_dmg + (a_real_dmg * a_crit_dmg_rate)
        print("Dealt Critical Damage: {:.2f}".format(a_real_dmg))
    
    else:
        a_real_dmg = random.uniform(a_dmg, a_normal_dmg)
    
    return a_rate, a_crit_dmg_rate, a_real_dmg


def get_enemy_crit(e_dmg):
  
    e_rate = random.uniform(0.1, 0.5)
    e_crit_dmg_rate = random.uniform(1.5, 2.0)

    e_normal_dmg = e_dmg + (e_dmg * e_rate)

    if e_rate > 0.80:
        e_real_dmg = e_real_dmg + (e_real_dmg * e_crit_dmg_rate)
        print("Dealt critical blow: {:.2f}".format(e_real_dmg))
    e_real_dmg = random.uniform(e_dmg, e_normal_dmg)

    return e_rate, e_crit_dmg_rate, e_real_dmg




'''

def attack(agent, agent_health, agent_damage, enemy, enemy_health, enemy_damage):
    # while (agent_health and enemy_health) >= 0:
    while True:
        
        var_enemy_damage = random.randint(7, enemy_damage)
        # print(var_enemy_damage)

        var_agent_damage = random.randint(11, agent_damage)
        # print(var_agent_damage)

        if (agent_health <= 0) or (enemy_health <= 0):
            break
        

        '''
'''
        
        if a_crit_rate >= 0.75:
            agent_damage += a_add_damage

        enemy_health -= var_agent_damage
        print(f"\n{agent} did {var_agent_damage} damage to {enemy}, {enemy}'s remaining health is {enemy_health}")

        agent_health -= var_enemy_damage
        print(f"{enemy} did {var_enemy_damage} damage to {agent}, {agent}'s remaining health is {agent_health}")

        time.sleep(1)
'''


    # if (agent_health or enemy_health) <= 0.0: # -> Since we are working with float values we write 0.0 instead of 0
    #     break
    
