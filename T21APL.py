# Default consumables
potion=prolonged_power
flask=seventh_demon
food=lavish_suramar_feast
augmentation=defiled

# This default action priority list is automatically created based on your character.
# It is a attempt to provide you with a action list that is both simple and practicable,
# while resulting in a meaningful and good simulation. It may not result in the absolutely highest possible dps.
# Feel free to edit, adapt and improve it to your own needs.
# SimulationCraft is always looking for updates and improvements to the default action lists.

# Executed before combat begins. Accepts non-harmful actions only.
actions.precombat=flask
actions.precombat+=/food
actions.precombat+=/augmentation
# Snapshot raid buffed stats before combat begins and pre-potting is done.
actions.precombat+=/snapshot_stats
actions.precombat+=/potion
actions.precombat+=/chi_burst
actions.precombat+=/chi_wave

# Executed every time the actor is available.
actions=auto_attack
actions+=/spear_hand_strike,if=target.debuff.casting.react
actions+=/touch_of_karma,interval=90,pct_health=0.5
actions+=/potion,if=buff.serenity.up|buff.storm_earth_and_fire.up|(!talent.serenity.enabled&trinket.proc.agility.react)|buff.bloodlust.react|target.time_to_die<=60
actions+=/touch_of_death,if=target.time_to_die<=9
actions+=/call_action_list,name=serenity,if=(talent.serenity.enabled&cooldown.serenity.remains<=0)|buff.serenity.up
actions+=/call_action_list,name=sef,if=!talent.serenity.enabled&(buff.storm_earth_and_fire.up|cooldown.storm_earth_and_fire.charges=2)
actions+=/call_action_list,name=sef,if=!talent.serenity.enabled&equipped.drinking_horn_cover&(cooldown.strike_of_the_windlord.remains<=18&cooldown.fists_of_fury.remains<=12&chi>=3&cooldown.rising_sun_kick.remains<=1|target.time_to_die<=25|cooldown.touch_of_death.remains>112)&cooldown.storm_earth_and_fire.charges=1
actions+=/call_action_list,name=sef,if=!talent.serenity.enabled&!equipped.drinking_horn_cover&(cooldown.strike_of_the_windlord.remains<=14&cooldown.fists_of_fury.remains<=6&chi>=3&cooldown.rising_sun_kick.remains<=1|target.time_to_die<=15|cooldown.touch_of_death.remains>112)&cooldown.storm_earth_and_fire.charges=1
actions+=/call_action_list,name=aoe,if=active_enemies>3
actions+=/call_action_list,name=st,if=active_enemies<=3

actions.aoe=call_action_list,name=cd
actions.aoe+=/energizing_elixir,if=!prev_gcd.1.tiger_palm&chi<=1&(cooldown.rising_sun_kick.remains=0|(artifact.strike_of_the_windlord.enabled&cooldown.strike_of_the_windlord.remains=0)|energy<50)
actions.aoe+=/arcane_torrent,if=chi.max-chi>=1&energy.time_to_max>=0.5
actions.aoe+=/fists_of_fury,if=talent.serenity.enabled&!equipped.drinking_horn_cover&cooldown.serenity.remains>=5&energy.time_to_max>2
actions.aoe+=/fists_of_fury,if=talent.serenity.enabled&equipped.drinking_horn_cover&(cooldown.serenity.remains>=15|cooldown.serenity.remains<=4)&energy.time_to_max>2
actions.aoe+=/fists_of_fury,if=!talent.serenity.enabled&energy.time_to_max>2
actions.aoe+=/fists_of_fury,if=cooldown.rising_sun_kick.remains>=3.5&chi<=5
actions.aoe+=/whirling_dragon_punch
actions.aoe+=/strike_of_the_windlord,if=!talent.serenity.enabled|cooldown.serenity.remains>=10
actions.aoe+=/rising_sun_kick,target_if=cooldown.whirling_dragon_punch.remains>=gcd&!prev_gcd.1.rising_sun_kick&cooldown.fists_of_fury.remains>gcd
actions.aoe+=/rushing_jade_wind,if=chi.max-chi>1&!prev_gcd.1.rushing_jade_wind
actions.aoe+=/chi_burst,if=chi<=3&(cooldown.rising_sun_kick.remains>=5|cooldown.whirling_dragon_punch.remains>=5)&energy.time_to_max>1
actions.aoe+=/chi_burst
actions.aoe+=/spinning_crane_kick,if=(active_enemies>=3|(buff.bok_proc.up&chi=chi.max))&!prev_gcd.1.spinning_crane_kick&set_bonus.tier21_4pc
actions.aoe+=/spinning_crane_kick,if=active_enemies>=3&!prev_gcd.1.spinning_crane_kick
actions.aoe+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.blackout_kick&chi.max-chi>=1&set_bonus.tier21_4pc&(!set_bonus.tier19_2pc|talent.serenity.enabled)
actions.aoe+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=(chi>1|buff.bok_proc.up|(talent.energizing_elixir.enabled&cooldown.energizing_elixir.remains<cooldown.fists_of_fury.remains))&((cooldown.rising_sun_kick.remains>1&(!artifact.strike_of_the_windlord.enabled|cooldown.strike_of_the_windlord.remains>1)|chi>4)&(cooldown.fists_of_fury.remains>1|chi>2)|prev_gcd.1.tiger_palm)&!prev_gcd.1.blackout_kick
actions.aoe+=/crackling_jade_lightning,if=equipped.the_emperors_capacitor&buff.the_emperors_capacitor.stack>=19&energy.time_to_max>3
actions.aoe+=/crackling_jade_lightning,if=equipped.the_emperors_capacitor&buff.the_emperors_capacitor.stack>=14&cooldown.serenity.remains<13&talent.serenity.enabled&energy.time_to_max>3
actions.aoe+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.blackout_kick&chi.max-chi>=1&set_bonus.tier21_4pc&buff.bok_proc.up
actions.aoe+=/tiger_palm,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&(chi.max-chi>=2|energy.time_to_max<3)
actions.aoe+=/tiger_palm,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&energy.time_to_max<=1&chi.max-chi>=2
actions.aoe+=/chi_wave,if=chi<=3&(cooldown.rising_sun_kick.remains>=5|cooldown.whirling_dragon_punch.remains>=5)&energy.time_to_max>1
actions.aoe+=/chi_wave

actions.cd=invoke_xuen_the_white_tiger
actions.cd+=/blood_fury
actions.cd+=/berserking
actions.cd+=/arcane_torrent,if=chi.max-chi>=1&energy.time_to_max>=0.5
actions.cd+=/lights_judgment
actions.cd+=/touch_of_death,cycle_targets=1,max_cycle_targets=2,if=!artifact.gale_burst.enabled&equipped.hidden_masters_forbidden_touch&!prev_gcd.1.touch_of_death
actions.cd+=/touch_of_death,if=!artifact.gale_burst.enabled&!equipped.hidden_masters_forbidden_touch
actions.cd+=/touch_of_death,cycle_targets=1,max_cycle_targets=2,if=artifact.gale_burst.enabled&((talent.serenity.enabled&cooldown.serenity.remains<=1)|chi>=2)&(cooldown.strike_of_the_windlord.remains<8|cooldown.fists_of_fury.remains<=4)&cooldown.rising_sun_kick.remains<7&!prev_gcd.1.touch_of_death

actions.sef=tiger_palm,target_if=debuff.mark_of_the_crane.down,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&energy=energy.max&chi<1
actions.sef+=/arcane_torrent,if=chi.max-chi>=1&energy.time_to_max>=0.5
actions.sef+=/call_action_list,name=cd
actions.sef+=/storm_earth_and_fire,if=!buff.storm_earth_and_fire.up
actions.sef+=/call_action_list,name=aoe,if=active_enemies>3
actions.sef+=/call_action_list,name=st,if=active_enemies<=3

actions.serenity=tiger_palm,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&energy=energy.max&chi<1&!buff.serenity.up
actions.serenity+=/call_action_list,name=cd
actions.serenity+=/serenity
actions.serenity+=/rising_sun_kick,target_if=min:debuff.mark_of_the_crane.remains,if=active_enemies<3
actions.serenity+=/strike_of_the_windlord
actions.serenity+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=(!prev_gcd.1.blackout_kick)&(prev_gcd.1.strike_of_the_windlord|prev_gcd.1.fists_of_fury)&active_enemies<2
actions.serenity+=/fists_of_fury,if=((equipped.drinking_horn_cover&buff.pressure_point.remains<=2&set_bonus.tier20_4pc)&(cooldown.rising_sun_kick.remains>1|active_enemies>1)),interrupt=1
actions.serenity+=/fists_of_fury,if=((!equipped.drinking_horn_cover|buff.bloodlust.up|buff.serenity.remains<1)&(cooldown.rising_sun_kick.remains>1|active_enemies>1)),interrupt=1
actions.serenity+=/spinning_crane_kick,if=active_enemies>=3&!prev_gcd.1.spinning_crane_kick
actions.serenity+=/rushing_jade_wind,if=!prev_gcd.1.rushing_jade_wind&buff.rushing_jade_wind.down&buff.serenity.remains>=4
actions.serenity+=/rising_sun_kick,target_if=min:debuff.mark_of_the_crane.remains,if=active_enemies>=3
actions.serenity+=/rushing_jade_wind,if=!prev_gcd.1.rushing_jade_wind&buff.rushing_jade_wind.down&active_enemies>1
actions.serenity+=/spinning_crane_kick,if=!prev_gcd.1.spinning_crane_kick
actions.serenity+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.blackout_kick

actions.serenity_opener=tiger_palm,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&energy=energy.max&chi<1&!buff.serenity.up&cooldown.fists_of_fury.remains<=0
actions.serenity_opener+=/arcane_torrent,if=chi.max-chi>=1&energy.time_to_max>=0.5
actions.serenity_opener+=/call_action_list,name=cd,if=cooldown.fists_of_fury.remains>1
actions.serenity_opener+=/serenity,if=cooldown.fists_of_fury.remains>1
actions.serenity_opener+=/rising_sun_kick,target_if=min:debuff.mark_of_the_crane.remains,if=active_enemies<3&buff.serenity.up
actions.serenity_opener+=/strike_of_the_windlord,if=buff.serenity.up
actions.serenity_opener+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=(!prev_gcd.1.blackout_kick)&(prev_gcd.1.strike_of_the_windlord)
actions.serenity_opener+=/fists_of_fury,if=cooldown.rising_sun_kick.remains>1|buff.serenity.down,interrupt=1
actions.serenity_opener+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=buff.serenity.down&chi<=2&cooldown.serenity.remains<=0&prev_gcd.1.tiger_palm
actions.serenity_opener+=/tiger_palm,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&chi=1

actions.st=call_action_list,name=cd
actions.st+=/energizing_elixir,if=!prev_gcd.1.tiger_palm&chi<=1&(cooldown.rising_sun_kick.remains=0|(artifact.strike_of_the_windlord.enabled&cooldown.strike_of_the_windlord.remains=0)|energy<50)
actions.st+=/arcane_torrent,if=chi.max-chi>=1&energy.time_to_max>=0.5
actions.st+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.blackout_kick&chi.max-chi>=1&set_bonus.tier21_4pc&buff.bok_proc.up
actions.st+=/tiger_palm,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&energy.time_to_max<=1&chi.max-chi>=2
actions.st+=/strike_of_the_windlord,if=!talent.serenity.enabled|cooldown.serenity.remains>=10
actions.st+=/whirling_dragon_punch
actions.st+=/rising_sun_kick,target_if=min:debuff.mark_of_the_crane.remains,if=((chi>=3&energy>=40)|chi>=5)&(!talent.serenity.enabled|cooldown.serenity.remains>=6)
actions.st+=/fists_of_fury,if=talent.serenity.enabled&!equipped.drinking_horn_cover&cooldown.serenity.remains>=5&energy.time_to_max>2
actions.st+=/fists_of_fury,if=talent.serenity.enabled&equipped.drinking_horn_cover&(cooldown.serenity.remains>=15|cooldown.serenity.remains<=4)&energy.time_to_max>2
actions.st+=/fists_of_fury,if=!talent.serenity.enabled&energy.time_to_max>2
actions.st+=/fists_of_fury,if=cooldown.fists_of_fury.duration<=cooldown.rising_sun_kick.remains
actions.st+=/rising_sun_kick,target_if=min:debuff.mark_of_the_crane.remains,if=!talent.serenity.enabled|cooldown.serenity.remains>=5
actions.st+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.blackout_kick&chi.max-chi>=1&set_bonus.tier21_4pc&(!set_bonus.tier19_2pc|talent.serenity.enabled)
actions.st+=/spinning_crane_kick,if=(active_enemies>=3|(buff.bok_proc.up&chi=chi.max))&!prev_gcd.1.spinning_crane_kick&set_bonus.tier21_4pc
actions.st+=/crackling_jade_lightning,if=equipped.the_emperors_capacitor&buff.the_emperors_capacitor.stack>=19&energy.time_to_max>3
actions.st+=/crackling_jade_lightning,if=equipped.the_emperors_capacitor&buff.the_emperors_capacitor.stack>=14&cooldown.serenity.remains<13&talent.serenity.enabled&energy.time_to_max>3
actions.st+=/spinning_crane_kick,if=active_enemies>=3&!prev_gcd.1.spinning_crane_kick
actions.st+=/rushing_jade_wind,if=chi.max-chi>1&!prev_gcd.1.rushing_jade_wind
actions.st+=/blackout_kick,target_if=min:debuff.mark_of_the_crane.remains,if=(chi>1|buff.bok_proc.up|(talent.energizing_elixir.enabled&cooldown.energizing_elixir.remains<cooldown.fists_of_fury.remains))&((cooldown.rising_sun_kick.remains>=1.5&(!artifact.strike_of_the_windlord.enabled|cooldown.strike_of_the_windlord.remains>1)|chi>4)&cooldown.fists_of_fury.remains>=1.5|prev_gcd.1.tiger_palm)&!prev_gcd.1.blackout_kick
actions.st+=/chi_wave,if=chi<=3&(cooldown.rising_sun_kick.remains>=5|cooldown.whirling_dragon_punch.remains>=5)&energy.time_to_max>1
actions.st+=/chi_burst,if=chi<=3&(cooldown.rising_sun_kick.remains>=5|cooldown.whirling_dragon_punch.remains>=5)&energy.time_to_max>1
actions.st+=/tiger_palm,target_if=min:debuff.mark_of_the_crane.remains,if=!prev_gcd.1.tiger_palm&!prev_gcd.1.energizing_elixir&(chi.max-chi>=2|energy.time_to_max<3)
actions.st+=/chi_wave
actions.st+=/chi_burst
