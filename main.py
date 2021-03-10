import pymem
import pymem.process
import keyboard
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
m_iCrosshairId = (0xB3E4)
dwForceAttack = (0x31D446C)


def main():
    isactive = False
    isactive2 = False
    isactive3 = False
    print("CoxPePaine")
    print("GLOW: PRESS N TO START, H TO STOP")
    print("BHOP: JUST HOLD SPACE")
    print("RADAR: PRESS [ TO START, ] TO STOP")
    print("NOFLASH: PRESS . TO START, ; TO STOP")

    pm = pymem.Pymem("csgo.exe")
    client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
    while True:

        ##### BHOP #####

        if keyboard.is_pressed("Space"):
            forcejump = client + dwForceJump
            localplayer = pm.read_int(client + dwLocalPlayer)
            if localplayer:
                ongr = pm.read_int(localplayer + m_fFlags)
                if ongr and ongr == 257:
                    pm.write_int(forcejump, 5)
                    time.sleep(0.08)
                    pm.write_int(forcejump, 4)

            time.sleep(0.002)

        ##### NOFLASH #####

        if keyboard.is_pressed(".") == True:
            isactive2 = True
            print("\n\nNOFLASH ACTIVE")
            time.sleep(0.5)
        if keyboard.is_pressed(";") == True:
            isactive2 = False
            print("\n\nNOFLASH STOPPED")
            time.sleep(0.5)

        if isactive2 == True:
            localplayer = pm.read_int(client + dwLocalPlayer)
            if localplayer:
                flash = localplayer + m_flFlashMaxAlpha
                if flash:
                    pm.write_float(flash, float(69.420))
        elif isactive2 == False:
            localplayer = pm.read_int(client + dwLocalPlayer)
            if localplayer:
                flash = localplayer + m_flFlashMaxAlpha
                if flash:
                    pm.write_float(flash, float(255))

        ##### RADAR #####

        if keyboard.is_pressed("[") == True:
            isactive3 = True
            print("\n\nRADAR ACTIVE")
            time.sleep(0.5)
        if keyboard.is_pressed("]") == True:
            isactive3 = False
            print("\n\nRADAR STOPPED")
            time.sleep(0.5)
        if isactive3 == True:
            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)
                localplayer = pm.read_int(client + dwLocalPlayer)
                localplayer_team = pm.read_int(localplayer + m_iTeamNum)
                if entity:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    if entity_team_id != localplayer_team:
                        pm.write_int(entity + m_bSpotted, 1)
        elif isactive3 == False:
            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)
                localplayer = pm.read_int(client + dwLocalPlayer)
                localplayer_team = pm.read_int(localplayer + m_iTeamNum)
                if entity:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    if entity_team_id != localplayer_team:
                        pm.write_int(entity + m_bSpotted, 0)

        ##### WALLHACK #####

        if keyboard.is_pressed("N") == True:
            isactive = True
            print("\n\nWALLHACK ACTIVE")
            time.sleep(0.5)

        if keyboard.is_pressed("H") == True:
            isactive = False
            print("\n\nWALLHACK STOPPED")
            time.sleep(0.5)

        if isactive == True:
            glow_manager = pm.read_int(client + dwGlowObjectManager)

            for i in range(1, 32):
                entity = pm.read_int(client + dwEntityList + i * 0x10)

                if entity:
                    entity_team_id = pm.read_int(entity + m_iTeamNum)
                    entity_glow = pm.read_int(entity + m_iGlowIndex)

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
##### TRIGGER #####

        if keyboard.is_pressed("alt"):
            entity_id = pm.read_int(localplayer + m_iCrosshairId)
            entity = pm.read_int(client + dwEntityList + (entity_id - 1) * 0x10)

            entity_team = pm.read_int(entity + m_iTeamNum)


            if entity_id > 0 and entity_id <= 64 and localplayer_team != entity_team:
                pm.write_int(client + dwForceAttack, 6)



if __name__ == '__main__':
    main()
