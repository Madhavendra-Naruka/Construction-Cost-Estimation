# Pre_Construction
from Pre_Construction.land_acquisition import land_acquisition
from Pre_Construction.design_and_planning import design_and_planning

#Construction
from Construction.site_preparation import site_preparation
from Construction.foundation import foundation
from Construction.superstructure import superstructure
from Construction.exterior_work import  exterior_work
from Construction.interior_work import interior_work
from Construction.building_systems import building_systems

#Post_Construction
from Post_Construction.finishing_touches import finishing_touches
from Post_Construction.inspections_handover import inspections_handover
from Post_Construction.maintenance_operation import maintenance_operation

CHECK_MARK = "✔"

land_acquisition_cost=None
design_and_planning_cost=None

site_preparation_cost=None
foundation_cost=None
superstructure_cost=None
exterior_work_cost=None
interior_work_cost=None
building_systems_cost=None

finishing_touches_cost=None
inspections_handover_cost=None
maintenance_operation_cost=None

pre_construction_menu_list=["1. Land Acquisition","2. Design and Planning","3. Back to Main Menu"]
def pre_construction_menu():
    # [print(e) for e in pre_construction_menu_list]
    print("Select a Sub-Phase :")
    [print(e) for e in pre_construction_menu_list]
    sub_phase =int(input("\n"))

    if sub_phase == 1:
        land_acquisition_cost = land_acquisition()
        pre_construction_menu_list[0]="1. Land Acquisition (✔) : " +str(land_acquisition_cost)
        pre_construction_menu()
    elif sub_phase == 2:
        design_and_planning_cost = design_and_planning()
        pre_construction_menu_list[1] = "2. Design and Planning (✔) : " + str(design_and_planning_cost)
        pre_construction_menu()
    elif sub_phase == 3:
        main_menu()
    else:
        print("Enter a valid input ! ! !\n")
        pre_construction_menu()
def construction_menu():
    sub_phase = int(input("Select a Sub-Phase : \n1. Site Preparation \n2. Foundation \n3. Superstructure \n4. Exterior Work \n5. Interior Work \n6. Building Systems \n7. Back to Main Menu \n\n"))
    if sub_phase==1:
        site_preparation_cost=site_preparation()
    elif sub_phase==2:
        foundation_cost=foundation()
    elif sub_phase ==3:
        superstructure_cost=superstructure()
    elif sub_phase ==4:
        exterior_work_cost=exterior_work()
    elif sub_phase ==5:
        interior_work_cost=interior_work()
    elif sub_phase ==6:
        building_systems_cost=building_systems()
    elif sub_phase ==7:
        main_menu()
    else:
        print("Enter a valid input ! ! !\n")
        construction_menu()
def post_construction_menu():
    sub_phase = int(input("Select a Sub-Phase : \n1. Finishing Touches \n2. Inspections and Handover \n3. Maintenance and Operation \n4. Back to Main Menu \n\n"))

    if sub_phase==1:
        finishing_touches_cost=finishing_touches()
    elif sub_phase==2:
        inspections_handover_cost=inspections_handover()
    elif sub_phase ==3:
        maintenance_operation_cost=maintenance_operation()
    elif sub_phase ==4:
        main_menu()
    else:
        print("Enter a valid input ! ! !\n")
        post_construction_menu()

def main_menu():
    phase=int(input("Select a Phase : \n1. Pre-Construction Phase \n2. Construction Phase \n3. Post-Construction Phase \n4. Exit\n\n"))

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


main_menu()