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

land_acquisition_cost=0
design_and_planning_cost=0

site_preparation_cost=0
foundation_cost=0
superstructure_cost=0
exterior_work_cost=0
interior_work_cost=0
building_systems_cost=0

finishing_touches_cost=0
inspections_handover_cost=0
maintenance_operation_cost=0

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
        site_preparation_cost=site_preparation()
        construction_menu_list[0]="1. Site Preparation (✔) : "+str(site_preparation_cost)
        construction_menu()
    elif sub_phase==2:
        foundation_cost=foundation()
        construction_menu_list[1]="2. Foundation (✔) : "+str(foundation_cost)
        construction_menu()
    elif sub_phase ==3:
        superstructure_cost=superstructure()
        construction_menu_list[2]="3. Superstructure (✔) : "+str(superstructure_cost)
        construction_menu()
    elif sub_phase ==4:
        exterior_work_cost=exterior_work()
        construction_menu_list[3]="4. Exterior Work (✔) : "+str(exterior_work_cost)
        construction_menu()
    elif sub_phase ==5:
        interior_work_cost=interior_work()
        construction_menu_list[4]="5. Interior Work (✔) : "+str(interior_work_cost)
        construction_menu()
    elif sub_phase ==6:
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
        finishing_touches_cost=finishing_touches()
        post_construction_menu_list[0]="1. Finishing Touches (✔) : "+str(finishing_touches_cost)
        post_construction_menu()
    elif sub_phase==2:
        inspections_handover_cost=inspections_handover()
        post_construction_menu_list[1]="2. Inspections and Handover (✔) : "+str(inspections_handover_cost)
        post_construction_menu()
    elif sub_phase ==3:
        maintenance_operation_cost=maintenance_operation()
        post_construction_menu_list[2]="3. Maintenance and Operation (✔) : "+str(maintenance_operation_cost)
        post_construction_menu()
    elif sub_phase ==4:
        main_menu()
    else:
        print("Enter a valid input ! ! !\n")
        post_construction_menu()
main_menu_list=["1. Pre-Construction Phase","2. Construction Phase","3. Post-Construction Phase","4. Exit"]
def update_main_menu_list():
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
def main_menu():
    print("Select a Phase :")
    update_main_menu_list()
    [print(e) for e in main_menu_list]
    print(main_menu_list)

    phase = int(input("\n"))
    if phase==1:
        pre_construction_menu()
    elif phase==2:
        construction_menu()
    elif phase==3:
        post_construction_menu()
    elif phase==4:
        pass
    else:
        print("Enter a valid input ! ! !\n")
        main_menu()

print("Hello, Welcome to Construction Project Estimation (CLI)\n")
main_menu()