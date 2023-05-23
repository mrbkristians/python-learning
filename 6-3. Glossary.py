workers = {
    "sam": "director",
    "anna": "massiere",
    "sonja": "counter",
    "lucia": "secretare",
}
best_workers = ["lucia"]

print("\n")

for worker, position in workers.items():
    print(f"Meet {worker.title()}.")
    print(f"Is a {position} of our company.")
    print("\n")

for worker in sorted(workers):
    print(f"Meet {worker.title()}")
print("\n")

print("Company is formed of differet position:")
for position in set(workers.values()):
    print(f"{position.title()},")
print("All they responcible for they position")
print("\n")

for  worker in workers:
    if worker in best_workers:
        print(f"Great job, have fun {worker.title()}")
        print(f"{worker.title()} This month Recieve Bonus")
        if worker == "lucia":
            print("Have fun babe")
    else: 
         print(f"Great job, have fun {worker.title()}")
print("\n")
        

       
