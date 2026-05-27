from agent_dataset import agent_data
from enemy_dataset import enemy_data
from mechanics import get_enemy, get_agent, attack, agent_list, get_agent_menu


print(f"\n1) Start\n2) Exit\n")
choice = input("Select the menu: ")
if int(choice) != 1:
    exit()
print("You have started the game!!\n")

enemy, enemy_health, enemy_damage = get_enemy(enemy_data)

print(f"\n<--Character Menu-->")

agent_l = agent_list(agent_data)

get_agent_menu(agent_l)

agent, agent_health, agent_damage = get_agent(agent_data, agent_l)

attack(agent, agent_health, agent_damage, enemy, enemy_health, enemy_damage)
