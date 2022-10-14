scene = 'think'
backpack = ['axe', 'compass', 'rations']

game_running = True

talk_act = True

axe_act = True

compass_act = True

rations_act = True

#talk or move to the ice cave, "use items" are the same,no mountain
#for best gameplay-> talk, use item, move to cave, talk there,  use item, move to tundra, talk

while game_running == True:
    
    while scene == 'think':
        print("you find yourself in an unfamiliar planet made of blue ice and snow under a beautiful starry night")
        enter_to_continue = input("press enter to continue")
        speaker_list = ['..']
        movement_list = ['ice cave, tundra, mountain']
        
        # menu of options
        action = input("You can:\n1).   'talk'\n2).   'move'\n3).   'use item'\n")
        
        if action == 'talk':
            if talk_act == True:
                print("as you speak, you can see the condensation from your breath")
                input("an unknown creature howls from somewhere..")
                talk_act = False
                continue
                
                    
            if talk_act == False:
                print ("you can't do that now")
                continue
        
        elif action == "move":
            print("You can move to: ", movement_list)
            move = input("where do you want to go?")
            
            if move == 'ice cave':
                scene = "ice cave"
            elif move == 'tundra':
                scene = "tundra"
            elif move == 'mountain':
                scene = "mountain"
        
        elif action == "use item":
            print("inventory: ", backpack)
            use = input("what do you want to use?")
            
            
            
            if use == 'axe':
                
                if axe_act == True:
                    print("the axe is in pristine condition..")
                    input("made of a very strong but unfamiliar material")
                    input("you put the axe back for a while, you wouldn't want to drop it")
                    backpack.remove('axe')
                    axe_act = False
                   
                    
                elif axe_act == False:
                    print("can't do that now")
                    input("...you wouldn't want to risk dropping your axe")
                   
                
            if use =='compass':
                
                if compass_act == True:
                    print ("the compass is erratic, this planet's magnetic field is odd")
                    input("the compass points towards a distant cave")
                    backpack.remove('compass')
                    compass_act = False
                    
                elif compass_act == False:
                    print("the compass has pointed to the cave")
                    input('holding the compass anylonger may strain the pointer, you put it back in your bag before it might be damaged')
                    
                    
            if use =='rations':
                
                if rations_act == True:
                    print("you pull out a block of dehydrated food..")
                    input("it seems to be of no use as you aren't hungry")
                    backpack.remove('rations')
                    rations_act = False
                
                elif rations_act == False:
                    print("the rations would be better kept in the bag")
                    input("you quickly put it away in fear of unknown creatures who might sense it")
                
            #ideally I would say if there is nothing in the bag print there aint nothing 
            if backpack == []:
                print ('your inventory is currently of no use to you, they might be of better use elsewhere')
            
    
    while scene == 'tundra':
        #same as ice cave
        
        print('You tread to the barren tundra filled with giant ice spikes the size of buildings protruding from the surface')
        input('a slight breeze brushes by')
        input('you take notice of foot prints which seem to show a bipedal three toed animal')
        speaker_list = ['..']
        movement_list = ['ice cave, tundra, mountain']
        
        # menu of options, again
        action = input("You can:\n1).   'talk'\n2).   'move'\n3).   'use item'\n")
        
        if action == 'talk':
            if talk_act == True:
                print("as you speak, you can see the condensation from your breath")
                input('"these tracks are the same tracks made from a native mammal specie, which are both domesticated and ridden as mounts"')
                talk_act = False
                continue
                
                    
            if talk_act == False:
                print ("you can't do that now")
                continue
        
        elif action == "move":
            print("You can move to: ", movement_list)
            move = input("where do you want to go?")
            
            if move == 'ice cave':
                scene = "ice cave"
            elif move == 'tundra':
                print("you are already in the tundra")
            elif move == 'mountain':
                scene = "mountain"
            continue
        
        elif action == "use item":
            print("inventory: ", backpack)
            use = input("what do you want to use?")
            
            if use == 'axe':
                print("the axe is in pristine condition..")
                input("made of a very strong but unfamiliar material")
            if use =='compass':
                print ("the compass is erratic, this planet's magnetic field is odd")
                input("the compass points down the cave")
            if use =='rations':
                print("you pull out a block of dehydrated food..")
                input("it seems to be of no use as you aren't hungry")
        
            
        continue
    
    while scene == 'mountain':
        
        print("for some reason, this mountian in particular already has a trail")
        enter_to_continue = input("press enter to continue")
        speaker_list = ['..']
        movement_list = ['ice cave, tundra, mountain']
        
        # menu of options
        action = input("You can:\n1).   'talk'\n2).   'move'\n3).   'use item'\n")
        
        if action == 'talk':
            if talk_act == True:
                print("as you speak, you can see the condensation from your breath")
                input("an unknown creature howls from somewhere..")
                talk_act = False
                continue
                
                    
            if talk_act == False:
                print ("you can't do that now")
                continue
        
        elif action == "move":
            print("You can move to: ", movement_list)
            move = input("where do you want to go?")
            
            if move == 'ice cave':
                scene = "ice cave"
            elif move == 'tundra':
                scene = "tundra"
            elif move == 'mountain':
                print('you are already here')
                continue
        
        elif action == "use item":
            print("inventory: ", backpack)
            use = input("what do you want to use?")
            
            if use == 'axe':
                print("the axe is in pristine condition..")
                input("made of a very strong but unfamiliar material")
            if use =='compass':
                print ("the compass is erratic, this planet's magnetic field is odd")
                input("the compass points towards a distant cave")
            if use =='rations':
                print("you pull out a block of dehydrated food..")
                input("it seems to be of no use as you aren't hungry")
    
    while scene == 'ice cave':
        print('You tread to the cave made of almost translucent ice')
        input('pieces of shiny gems and broken mining helments lay around its ent-rance, you reconize that they were issued by a recently collapsed government')
        input('your senses tell you that you are not alone inside here..')
        speaker_list = ['..']
        movement_list = ['ice cave, tundra, mountain']
        
        # menu of options, again
        action = input("You can:\n1).   'talk'\n2).   'move'\n3).   'use item'\n")
        
        
        
        if action == 'talk':
            if talk_act == True:
                print("as you speak, you can see the condensation from your breath")
                input("an unknown creature howls from somewhere..")
                talk_act = False
                continue
                
                    
            if talk_act == False:
                print ("you can't do that now")
                continue
        
        elif action == "move":
            print("You can move to: ", movement_list)
            move = input("where do you want to go?")
            
            if move == 'ice cave':
                print("you are already in the ice cave")
            elif move == 'tundra':
                scene = "tundra"
            elif move == 'mountain':
                scene = "mountain"
            continue
        
        elif action == "use item":
            print("inventory: ", backpack)
            use = input("what do you want to use?")
            
            if use == 'axe':
                print("the axe is in pristine condition..")
                input("made of a very strong but unfamiliar material")
            if use =='compass':
                print ("the compass is erratic, this planet's magnetic field is odd")
                input("the compass points down the cave")
            if use =='rations':
                print("you pull out a block of dehydrated food..")
                input("it seems to be of no use as you aren't hungry")
        
        
        continue
    # think scene --move and use item, ice cave --talk and use items,