from data_map import replaceable_items_map
from logic import find_quick_sub, find_all_chains

def start_app():
    print("--- Welcome to My Ingredient Finder AI ---")
    print("Items in my list:", ", ".join(replaceable_items_map.keys()))
    
    have_not = input("\nWhat ingredient are you missing? ")
    target = input("What are you trying to replace it with? ")

    if have_not in replaceable_items_map and target in replaceable_items_map:
        # Running the two AI searches
        short = find_quick_sub(replaceable_items_map, have_not, target)
        long_chain = find_all_chains(replaceable_items_map, have_not, target)

        print("\n[AI SEARCH RESULTS]")
        if short:
            print(f"Shortest Way (BFS): {' -> '.join(short)}")
            print(f"Full Chain (DFS): {' -> '.join(long_chain)}")
        else:
            print("No path found between these items.")
    else:
        print("I don't have that ingredient in my list yet!")

if __name__ == "__main__":
    start_app()