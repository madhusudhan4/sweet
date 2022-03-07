def print_emp(_id,_name,_sal,**kwargs):

    print(f"id:{_id},name:{_name},sal:{_sal}")
    for key,values in kwargs.items():
        print(f"{key}:{values}",end=" ")
    print()

print_emp(1200,'raju',12000)
print_emp(1233,'ram',13000,dept='econamy')
print_emp(1234,'kumar',14000,dep='english'  ,raju=233)