from tabulate import tabulate

# Pre_Construction
from Pre_Construction.land_acquisition import land_acquisition
from Pre_Construction.design_and_planning import design_and_planning

#Construction
from Construction.site_preparation import site_preparation
from Construction.foundation import foundation
from Construction.superstructure import superstructure
from Construction.exterior_work import exterior_work
from Construction.interior_work import interior_work
from Construction.building_systems import building_systems

#Post_Construction
from Post_Construction.finishing_touches import finishing_touches
from Post_Construction.inspections_handover import inspections_handover
from Post_Construction.maintenance_operation import maintenance_operation

CHECK_MARK = "✔"

land_acquisition_cost=5550000
design_and_planning_cost=645000

site_preparation_cost=50000
foundation_cost=50000000
superstructure_cost=1040450000
exterior_work_cost=45620000
interior_work_cost=4500000
building_systems_cost=45552860

finishing_touches_cost=5600000
inspections_handover_cost=250000
maintenance_operation_cost=1000000

pre_construction_total=0
construction_total=0
post_construction_total=0
pre_construction_menu_list=["1. Land Acquisition","2. Design and Planning","3. Back to Main Menu"]
def pre_construction_menu():
    # [print(e) for e in pre_construction_menu_list]
    print("Select a Sub-Phase :")
    [print(e) for e in pre_construction_menu_list]
    sub_phase =int(input("\n"))

    if sub_phase == 1:
        global land_acquisition_cost
        land_acquisition_cost = land_acquisition()
        pre_construction_menu_list[0]="1. Land Acquisition (✔) : " +str(land_acquisition_cost)
        pre_construction_menu()
    elif sub_phase == 2:
        global design_and_planning_cost
        design_and_planning_cost = design_and_planning()
        pre_construction_menu_list[1] = "2. Design and Planning (✔) : " + str(design_and_planning_cost)
        pre_construction_menu()
    elif sub_phase == 3:
        main_menu()
    else:
        print("Enter a valid input ! ! !\n")
        pre_construction_menu()
construction_menu_list=["1. Site Preparation","2. Foundation","3. Superstructure","4. Exterior Work","5. Interior Work","6. Building Systems","7. Back to Main Menu"]
def construction_menu():
    print("Select a Sub-Phase :")
    [print(e) for e in construction_menu_list]
    sub_phase =int(input("\n"))
    if sub_phase==1:
        global site_preparation_cost
        site_preparation_cost=site_preparation()
        construction_menu_list[0]="1. Site Preparation (✔) : "+str(site_preparation_cost)
        construction_menu()
    elif sub_phase==2:
        global foundation_cost
        foundation_cost=foundation()
        construction_menu_list[1]="2. Foundation (✔) : "+str(foundation_cost)
        construction_menu()
    elif sub_phase ==3:
        global superstructure_cost
        superstructure_cost=superstructure()
        construction_menu_list[2]="3. Superstructure (✔) : "+str(superstructure_cost)
        construction_menu()
    elif sub_phase ==4:
        global exterior_work_cost
        exterior_work_cost=exterior_work()
        construction_menu_list[3]="4. Exterior Work (✔) : "+str(exterior_work_cost)
        construction_menu()
    elif sub_phase ==5:
        global interior_work_cost
        interior_work_cost=interior_work()
        construction_menu_list[4]="5. Interior Work (✔) : "+str(interior_work_cost)
        construction_menu()
    elif sub_phase ==6:
        global building_systems_cost
        building_systems_cost=building_systems()
        construction_menu_list[5]="6. Building Systems (✔) : "+str(building_systems_cost)
        construction_menu()
    elif sub_phase ==7:
        main_menu()
    else:
        print("Enter a valid input ! ! !\n")
        construction_menu()

post_construction_menu_list=["1. Finishing Touches","2. Inspections and Handover","3. Maintenance and Operation","4. Back to Main Menu"]
def post_construction_menu():
    print("Select a Sub-Phase :")
    [print(e) for e in post_construction_menu_list]
    sub_phase = int(input("\n"))

    if sub_phase==1:
        global finishing_touches_cost
        finishing_touches_cost=finishing_touches()
        post_construction_menu_list[0]="1. Finishing Touches (✔) : "+str(finishing_touches_cost)
        post_construction_menu()
    elif sub_phase==2:
        global inspections_handover_cost
        inspections_handover_cost=inspections_handover()
        post_construction_menu_list[1]="2. Inspections and Handover (✔) : "+str(inspections_handover_cost)
        post_construction_menu()
    elif sub_phase ==3:
        global maintenance_operation_cost
        maintenance_operation_cost=maintenance_operation()
        post_construction_menu_list[2]="3. Maintenance and Operation (✔) : "+str(maintenance_operation_cost)
        post_construction_menu()
    elif sub_phase ==4:
        main_menu()
    else:
        print("Enter a valid input ! ! !\n")
        post_construction_menu()
def update_main_menu_list_amount():
    global pre_construction_total, construction_total, post_construction_total

    pre_construction_total=design_and_planning_cost+land_acquisition_cost
    construction_total=site_preparation_cost+foundation_cost+superstructure_cost+exterior_work_cost+interior_work_cost+building_systems_cost
    post_construction_total=finishing_touches_cost+inspections_handover_cost+maintenance_operation_cost
    if pre_construction_total>0:
        main_menu_list[0]="1. Pre-Construction Phase (✔) : "+str(pre_construction_total)
        print("updated")
    if construction_total>0:
        main_menu_list[1]="2. Construction Phase (✔) : "+str(construction_total)
    if post_construction_total>0:
        main_menu_list[2]="3. Post-Construction Phase (✔) : "+str(post_construction_total)


def cost_estimation_summary():
    print( "\n******* COST ESTIMATION SUMMARY *******\n")

    pre_construction_table = []
    # highlight_row("Pre-Construction Phase")
    pre_construction_summary=""
    if pre_construction_total > 0:
        pre_construction_summary = "*** Pre-Construction Phase ***\n"
        if land_acquisition_cost > 0:
            pre_construction_table.append(["  Land Acquisition", f"₹{land_acquisition_cost:,.2f}"])
        if design_and_planning_cost > 0:
            pre_construction_table.append(["  Design and Planning", f"₹{design_and_planning_cost:,.2f}"])
        pre_construction_table.append(["  Total", f"₹{pre_construction_total:,.2f}"])
    pre_construction_summary+=tabulate(pre_construction_table, headers=[], tablefmt="fancy_grid")
    print(pre_construction_summary)

    construction_table=[]
    construction_summary = ""
    if construction_total > 0:
        construction_summary="\n*** Construction Phase ***\n"
        if site_preparation_cost > 0:
            construction_table.append(["  Site Preparation", f"₹{site_preparation_cost:,.2f}"])
        if foundation_cost > 0:
            construction_table.append(["  Foundation", f"₹{foundation_cost:,.2f}"])
        if superstructure_cost > 0:
            construction_table.append(["  Superstructure", f"₹{superstructure_cost:,.2f}"])
        if exterior_work_cost > 0:
            construction_table.append(["  Exterior Work", f"₹{exterior_work_cost:,.2f}"])
        if interior_work_cost > 0:
            construction_table.append(["  Interior Work", f"₹{interior_work_cost:,.2f}"])
        if building_systems_cost > 0:
            construction_table.append(["  Building Systems", f"₹{building_systems_cost:,.2f}"])
        construction_table.append(["  Total", f"₹{construction_total:,.2f}"])
    construction_summary += tabulate(construction_table, headers=[], tablefmt="fancy_grid")
    print(construction_summary)

    post_construction_table=[]
    post_construction_summary=""
    if post_construction_total > 0:
        post_construction_summary = "\n*** Post-Construction Phase ***\n"
        if finishing_touches_cost > 0:
            post_construction_table.append(["  Finishing Touches", f"₹{finishing_touches_cost:,.2f}"])
        if inspections_handover_cost > 0:
            post_construction_table.append(["  Inspections and Handover", f"₹{inspections_handover_cost:,.2f}"])
        if maintenance_operation_cost > 0:
            post_construction_table.append(["  Maintenance and Operation", f"₹{maintenance_operation_cost:,.2f}"])
        post_construction_table.append(["  Total", f"${post_construction_total:,.2f}"])

    total_cost = pre_construction_total + construction_total + post_construction_total

    post_construction_summary += tabulate(post_construction_table, headers=[], tablefmt="fancy_grid")
    print(post_construction_summary)

    total_row = [[f"\nTotal Project Estimate :  ₹{total_cost:,.2f}\n".center(50)]]
    print(tabulate(total_row, headers=[], tablefmt="fancy_grid"))

main_menu_list=["1. Pre-Construction Phase","2. Construction Phase","3. Post-Construction Phase","4. Show Summary","5. Exit"]

def main_menu():
    print("Select a Phase :")
    update_main_menu_list_amount()
    [print(e) for e in main_menu_list]


    phase = int(input(""))
    if phase==1:
        pre_construction_menu()
    elif phase==2:
        construction_menu()
    elif phase==3:
        post_construction_menu()
    elif phase==4:
        cost_estimation_summary()
        main_menu()
    elif phase==5:
        pass
    else:
        print("Enter a valid input ! ! !\n")
        main_menu()

print("Hello, Welcome to Construction Project Estimation (CLI)\n")
main_menu()