def print_emp(_id,_name,_sal,**kwargs):
    print(f"eid{_id},ename{_name},esal{_sal}")
    for key,val in kwargs.items():
        print("  {key } : {val}",end=" ")
res = print_emp(124,"jhon",23000)
res = print_emp(123,"ram",12344)
res = print_emp(125,"madhu",300992)
print(res)