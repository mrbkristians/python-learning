guest_list = ["arturs", "richards", "rolands"]
party_type = "dinner"

print(f"\nGuest list for the {party_type}:\n\t{guest_list[0].title()}\n\t{guest_list[1].title()}\n\t{guest_list[2].title()}")

print(f"\n\tHi, dear {guest_list[0].title()}, I would like to invite you to a {party_type}.\n")
print(f"\n\tHi, dear {guest_list[1].title()}, I would like to invite you to a {party_type}.\n")
print(f"\n\tHi, dear {guest_list[2].title()}, I would like to invite you to a {party_type}.\n")

cant_make_it = "richards"
guest_list.remove(cant_make_it)

print(f"\n\tSadly, but {cant_make_it.title()} cannot make it,to a {party_type}\n")

new_guest = guest_list.insert(1, "jenots")

print(f"\nNew guest list:\n\t{guest_list[0].title()}\n\t{guest_list[1].title()}\n\t{guest_list[2].title()}\n")

print(f"\n\tHi, dear {guest_list[2].title()}, I would like to invite you to a {party_type}.\n")

abloms = guest_list.pop()

print(f"\n\tDiemžēls sanāča neparedzēta situācija un {abloms.title()} nevarēs ar mums pavakariņot.\n")

print(f"Total amount of guests: {len(guest_list)}!\n")
