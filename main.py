from agent_dataset import agent_data
from enemy_dataset import enemy_data
from mechanics import get_enemy, get_agent, agent_list, get_agent_menu, get_agent_crit, get_enemy_crit


print(f"\n1) Start\n2) Exit\n")
choice = input("Select the menu: ")
if int(choice) != 1:
    exit()
print("You have started the game!!\n")

enemy, enemy_health, enemy_damage = get_enemy(enemy_data)

print(f"Your enemy is: {enemy}")
print(f"Health is {enemy_health}")
print(f"Damage is {enemy_damage}\n")

# crit_rate_enemy, crit_damage_enemy = get_crit(enemy_damage)
# if crit_rate_enemy >= 0.75:
#     enemy_damage += crit_damage_enemy

print(f"\n<--Character Menu-->")
agent_l = agent_list(agent_data)
get_agent_menu(agent_l)

agent, agent_health, agent_damage = get_agent(agent_data, agent_l)


print("\nAgent Health is: {}".format(agent_health))
print("Agent Damage is: {}\n".format(agent_damage))

agent_crit_rate, agent_crit_damage_rate, upto_agent_damage = get_agent_crit(agent_damage)


print("{}'s crit rate multiplier is: {:.2f}".format(agent, agent_crit_rate))
print("{}'s crit damage multiplier is: {:.2f}".format(agent, agent_crit_damage_rate))
print("{}'s Damage is: {:.2f}".format(agent, upto_agent_damage))



enemy_crit_rate, enemy_crit_damage_rate, upto_enemy_damage = get_enemy_crit(enemy_damage)


print("\n{}'s crit rate multiplier is: {:.2f}".format(enemy, enemy_crit_rate))
print("{}'s crit damage multiplier is: {:.2f}".format(enemy, enemy_crit_damage_rate))
print("{}'s Damage is: {:.2f}\n".format(enemy, upto_enemy_damage))




import time
import random

# print("Agent health is {}".format(agent_health))
print("{} health is {}\n".format(agent, agent_health))

while True:

    # if (agent_health or enemy_health) <= 0.0: # -> Since we are working with float values we write 0.0 instead of 0
    #     break
    

    if agent_crit_rate > 0.80:
        real_enemy_damage = real_enemy_damage + (real_enemy_damage * enemy_crit_damage_rate)
        print("Dealt critical blow!!")
    else:
        real_enemy_damage = random.uniform(enemy_damage, upto_enemy_damage)
    
    agent_health -= real_enemy_damage
    real_agent_damage = random.uniform(agent_damage, upto_agent_damage)
    enemy_health -= real_agent_damage
    
    # if (agent_health or enemy_health) <= (real_agent_damage or real_enemy_damage): 
    #     break

    if (agent_health or enemy_health) < 0.0:
        agent_health == 0.0
        enemy_health == 0.0
        break

    print("{} dealt {:.2f} damage to {}, {}'s remaining health is {:.2f}".format(enemy, real_enemy_damage, agent, agent, agent_health))

    print("{} dealt {:.2f} damage to {}, {}'s remaining health is {:.2f}\n".format(agent, real_agent_damage, enemy, enemy, enemy_health))

    if agent_health <= enemy_damage: # 0.0:
        break
    if enemy_health <= agent_damage: # 0.0:
        break 

    time.sleep(0.5)

if agent_health > enemy_health:
    print("You win!")
else:
    print("You lose")



# crit_rate_agent, crit_damage_agent = get_crit(agent_damage)
# if crit_rate_agent >= 0.75:
#     agent_damage += crit_damage_agent

# attack(agent, agent_health, agent_damage, enemy, enemy_health, enemy_damage)
