dict = {
    "table1":
            {
                "total": 10,
                "month": "jul/22"
             },
        "table2":
            {
                "total": 5,
                "month": "ago/22"
            }
    }

print(f"dict {dict}")
print(f"item {dict['table1']}")

for item in dict:
    print(item)
    print(f"{item} {dict[item]['total']} {dict[item]['month']}")
