import pymem
import pymem.process
import keyboard
import os
import time

dwEntityList = (0x4DA2F24)
dwGlowObjectManager = (0x52EB518)
m_iGlowIndex = (0xA438)
m_iTeamNum = (0xF4)
dwLocalPlayer = (0xD8B2DC)
m_bSpotted = (0x93D)
dwForceJump = (0x524CE84)
m_fFlags = (0x104)
m_flFlashMaxAlpha = (0xA41C)


def main():
    isactive = False
    print("CoxPePaine")
    print("N pt a porni valu H pt a opri valu")
    print("Esti gay lmfao")

    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    while True:
        ##### BHOP #####
        if keyboard.is_pressed("Space"):
            forcejump = client + dwForceJump
            localplayer = pm.read_int(client + dwLocalPlayer)
            if localplayer:
                onground = pm.read_int(localplayer + m_fFlags)
                if onground and onground == 257:
                    pm.write_int(forcejump, 5)
                    time.sleep(0.08)
                    pm.write_int(forcejump, 4)

            time.sleep(0.002)
        ##### NOFLASH #####
        localplayer = pm.read_int(client + dwLocalPlayer)
        if localplayer:
            flash = localplayer + m_flFlashMaxAlpha
            if flash:
                pm.write_float(flash, float(0))
        ##### RADAR #####
        for i in range(1, 32):
            entity = pm.read_int(client + dwEntityList + i * 0x10)
            localplayer = pm.read_int(client + dwLocalPlayer)
            localplayer_team = pm.read_int(localplayer + m_iTeamNum)
            if entity:
                entity_team_id = pm.read_int(entity + m_iTeamNum)
                if entity_team_id != localplayer_team:
                    pm.write_int(entity + m_bSpotted, 1)
        ##### WALLHACK #####
        if keyboard.is_pressed("N") == True:
            isactive = True
            os.system("cls")
            os.system("color a")
            print("\n\n-_-A pornit janghina-_-")
            time.sleep(0.5)



        if keyboard.is_pressed("H") == True:
            isactive = False
            os.system("cls")
            os.system("color a")
            print("\n\n-_-S-a dus pe pula-_-")
            time.sleep(0.5)

        if isactive == True:
                glow_manager = pm.read_int(client + dwGlowObjectManager)

                for i in range(1, 32):
                    entity = pm.read_int(client + dwEntityList + i * 0x10)

                    if entity:
                        entity_team_id = pm.read_int(entity + m_iTeamNum)
                        entity_glow = pm.read_int(entity + m_iGlowIndex)
                        localplayer = pm.read_int(client + dwLocalPlayer)
                        localplayer_team = pm.read_int(localplayer + m_iTeamNum)


                        if entity_team_id == 2 and entity_team_id != localplayer_team:  # Terrorist
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)

                        elif entity_team_id == 3 and entity_team_id != localplayer_team:  # Counter-terrorist
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x4, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x8, float(0))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0xC, float(1))
                            pm.write_float(glow_manager + entity_glow * 0x38 + 0x10, float(1))
                            pm.write_int(glow_manager + entity_glow * 0x38 + 0x24, 1)





if __name__ == '__main__':
    main()