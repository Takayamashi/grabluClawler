import xpathtest
import csv_shape
import released_weapon
import skill_shape
import skill_effect
import skill_checker
import skill_effect_shape
import weapon_skill_shape

if __name__ == "__main__":
    xpathtest.weapon_ssr_list()
    xpathtest.weapon_ssr_list_released4()
    xpathtest.weapon_ssr_list_released5()
    xpathtest.weapon_skill_list()
    xpathtest.weapon_special()

    csv_shape.weapon_del()
    csv_shape.weapon_released4_del()
    csv_shape.weapon_released5_del()
    csv_shape.weapon_special_del()
    csv_shape.weapon_append()

    released_weapon.weapon_released5_list()
    released_weapon.weapon_released4_list()

    skill_shape.skill_shaped_list()

    skill_effect.skill_effect_normal_attack()
    skill_effect.skill_effect_maguna_attack()
    skill_effect.skill_effect_ex_attack()
    skill_effect.skill_effect_normal_defence()
    skill_effect.skill_effect_maguna_defence()
    skill_effect.skill_effect_bahamut()
    skill_effect.skill_effect_kamui()
    skill_effect.skill_effect_haisui()
    skill_effect.skill_effect_konshin()
    skill_effect.skill_effect_DATA()
    skill_effect.skill_effect_critical()

    skill_effect_shape.skill_effect_shaped_list()

    weapon_skill_shape.weapon_csv_making()
