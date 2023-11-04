#!/usr/bin/python
import random

from discord.ext import commands

META_LIST = [
    # Covert Sniper
    'Dragoon/Weaponry Tinkering Medium Sniper (Need Medic/External Stims) (DPS, Priority Control, Conc, ITD, Short Scout)',
    'Flower Child/Chemistry Running Medium Sniper (DPS, Priority Control, Conc, ITD, Short Scout)',
    # Field Medic
    'Energizer/Triage Hacking Heavy Medic (QM, Nano Rez-Sick, Heals, Adrenaline, Mender, Revive)',
    'Packrat/Triage Hacking Heavy Medic (QM, Nano Rez-Sick, Heals, Adrenaline, Mender, Revive)',
    # Tactician
    'Healer/Triage Hacking Heavy Tactician (QM, Heals, Endurance, Rad Away, Ion Cannon)',
    # Psychologist
    'Healer/Triage Hacking Heavy Psychologist (QM, Heals, MC/Moti)',
    # Maverick
    'Swift Learner/Robotics Hacking Heavy Chaingun+Mecha Maverick (Tank, Reactor Filling)',
    'Gadgeteer/Chemistry Hacking Heavy Rocket+Kami Maverick (Stims) (DPS, CC, Innard Control, Reactor Filling)',
    # Demolitions
    'Energizer/Energy Cells Toughness Heavy Demo (CC, Innard Control, Nuke, Mods)',
    # Cyborg
    'Acrobat/Cybernetics Running Cyborg (Tank, Stun, Reactor Filling, Short Scout)',
    'Acrobat/Power Armor Running Cyborg (Tank, Stun, Reactor Filling, Short Scout)',
    'Acrobat/Energy Cells Running Cyborg (Tank, Stun, Reactor Filling, Short Scout)',
    # Pyrotechnician
    'Energizer/Energy Cells Tinkering Pyrotechnician (CC, Priority Control, DPS, Short Scout, Commando Slayer)',
    # Watchman
    'Flower Child/Chemistry Toughness Watchman (Off Tank, DPS, Grenade, Commando Slayer, Short Scout, Nurse)',
    'Chem Reliant/Chemistry Toughness Watchman (Stims, Grenade, Commando Slayer, Short Scout, Nurse)',
    'Gadgeteer/Chemistry Toughness Watchman (Stims, Grenade, Commando Slayer, Short Scout, Nurse)',
    'Energizer/Energy Cells Tinkering Watchman (Surge, Grenade, Commando Slayer, Short Scout, Nurse)',
    # Tech Ops
    'Gadgeteer/Robotics Hacking Heavy Tech Ops (Off Tank, DPS, Short Scout, Rad Killer)',
    # Umbrella Clone
    'Chem Reliant/Chemistry Toughness Alice (Stims, CC, DPS, Innard Control, Shield, Umbrella Slayer)',
    'Gadgeteer/Chemistry Toughness Alice (Stims, CC, DPS, Innard Control, Shield, Umbrella Slayer)',
]

OFF_META_LIST = [
    # Covert Sniper
    'Energizer/Weaponry Tinkering Medium Sniper (Need Medic/External Stims)',
    'Engineer/Cybernetics Tinkering Medium Sniper (Dangerous for Noobs) (Need Medic/External Stims)',
    'Dragoon/Weaponry Tinkering Heavy Sniper (Heavy Armor Sniper is Dangerous for Noobs) (Need Medic/External Stims)',
    'Gadgeteer/Chemistry Running Medium Sniper (Stims) (DPS, Priority Control, Conc, ITD, Short Scout)',
    # Field Medic
    'Engineer/Triage Hacking Heavy Medic (Dangerous for Noobs) (QM, Nano Rez-Sick, Heals, Adrenaline, Mender, Revive)',
    # Tactician
    'Gadgeteer/Chemistry Hacking Heavy Tactician (Stims, Cadet, QM, Endurance, Rad Away, Ion Cannon)',
    'Engineer/Chemistry Hacking Heavy Tactician (Dangerous for Noobs), (Stims, Cadet, Endurance, Rad Away, Ion Cannon)',
    # Psychologist
    'Engineer/Triage Hacking Heavy Psychologist (QM, Heals, MC/Moti, Chrono, Stims)',
    'Flower Child/Chemistry Hacking Heavy Psychologist (QM, Heals, MC/Moti, Chrono, Nemesis Slay)',
    # Maverick
    'Flower Child/Chemistry Hacking Heavy Rocket+Kami Maverick (DPS, CC, Innard Control, Umbrella Slayer)',
    'X+Chrome Maverick (DPS, CC, Innard Control, Half Solo)',
    # Heavy Ordnance
    'Swift Learner/Robotics Running Heavy HO (DPS, Batteries, CC, Reactor Filling)',
    'Reckless/Robotics Running Heavy HO (DPS, Batteries, CC, Reactor Filling)',
    'Rad Resistant/Running Light HO (No Nanites) (DPS, Batteries, CC, Reactor Filling)',
    'Gadgeteer/Power Armor Heavy HO (Tank, DPS, Batteries, CC, Reactor Filling)',
    # Demolitions
    'Engineer/Energy Cells Toughness Heavy Demo (Dangerous for Noobs) (CC, Innard Control, Nuke, Mods)',
    'Packrat/Cybernetics Toughness Heavy Demo (QM)',
    'Reckless/Energy Cells Toughness Heavy Demo (Manual C4, CC, Innard Control, Nuke, Mods)'
    # Cyborg
    'Engineer/Energy Cells Running Cyborg (Tank, Stun, Reactor Filling, Short Scout)',
    'Energizer/Energy Cells Hacking Cyborg (Tank, Stun, Reactor Filling, Short Scout)',
    # Pyrotechnician
    'Engineer/Energy Cells Tinkering Pyrotechnician (Dangerous for Noobs) (CC, Priority Control, DPS, Short Scout, Commando Slayer)'
    # Watchman
    'Engineer/Energy Cells Tinkering Watchman (Dangerous for Noobs) (Surge, Grenade, Commando Slayer)',
    'Engineer/Chemistry Toughness Watchman (Dangerous for Noobs) (Stims, Grenade, Commando Slayer)',
    # Tech Ops
    'Reckless/Robotics Hacking Heavy Tech Ops (Off Tank, DPS, Short Scout, Rad Killer)',
    'Engineer/Robotics Hacking Heavy Tech Ops (Off Tank, DPS, Short Scout, Rad Killer)',
    'Energizer/Robotics Hacking Heavy Tech Ops (Off Tank, DPS, Short Scout, Rad Killer)',
    # Umbrella Clone
    'Acrobat/Cybernetics Toughness Heavy Alice (Need Medic/External Stims) (Tank, CC, DPS, Innard Control, Shield, Umbrella Slayer)',
]

META_SOLO_LIST = [
    # Heavy Ordnance
    'Rad Resistant/Espionage Light Running HO',
    # Watchman
    'Rad Resistant/Espionage Spotting Watchman (Grenade, Overdrive, Surge)',
    # Sniper
    'Flower Child/Chemistry Running Light Sniper',
    'Gadgeteer/Chemistry Running Light Sniper (Stims)',
    # Umbrella Clone
    'Rad Resistant/Espionage Light Alice',
]

OFF_META_SOLO_LIST = [
    # Covert Sniper
    'Gadgeteer/Chemistry Running Light Sniper (Stims) (DPS, Priority Control, Conc, ITD)',
    # Field Medic
    'Rad Resistant/Espionage Hacking Light Medic (Stims) (4 Gun, Nano Rez-Sick, Heals, Adrenaline, Mender, Revive)'
    # Tactician
    'Rad Resistant/Espionage Hacking Light Tactician (Stims) (4 Gun, Cadet, Endurance, Rad Away, Ion Cannon Scout)'
    # Psychologist
    'Rad Resistant/Espionage Hacking Light Psychologist (Stims) (4 Gun, MC/Moti)',
    # Maverick
    'X+C smav'
    # Heavy Ordnance
    'Reckless/Espionage Light Running HO (DPS, Batteries, CC, Reactor Filling)',
    # Demolitions
    'Rad Resistant/Espionage Light Running Demo (3 MIRV, C4, Nuke, Mods)'
    # Cyborg
    'Rad Resistant/Espionage Hacking Cyborg'
    # Pyrotechnician
    # Watchman
    'Flower Child/Chemistry Toughness Watchman (Off Tank, DPS, Grenade, Commando Slayer, Short Scout, Nurse)',
    # Tech Ops
    # Umbrella Clone
    'Chem Reliant/Espionage Light Alice (Stims)',
]

SLAP_LIST = [
    '{author} slapped {target} with a large tuna! Wet.',
    '{author} slapped {target} with a tasty cookie! Yum.',
    '{author} slapped {target} with both hands!',
    '{author} slapped {target} with a taco! Messy, but tasty.',

    '{author} slapped {target}. Ouch! That must hurt!',
    '{author} slapped {target}. That should teach you a lesson!',
    '{author} slapped {target}. Take that, you fool!',
    '{author} slapped {target}. Ooooh snap!',
    '{author} slapped {target}. Get slapped, son!',
    '{author} slapped {target}. Your bloody hipster!',
    '{author} slapped {target}. Go buy us some Ice Cream!',

    '{author} slayed {target}. Feel the pain!',
    '{author} drained {target}. Energy is for wimps!',
    '{author} teleported {target} away to a dark alley... Know your name!',
    '{author} ioned {target}. Calculated?',
    '{author} shockwaved {target}. Geometry.',
    '{author} x-naded {target}. Lethal!',

    '{author} tried to slap {target} but missed. Clumsy!',
]

class Roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='roll', help='Rolls a random term from a provided list (separated by space), or from a good Class from a pre-selected list.')
    async def roll(self, ctx, *elements):
        list = elements or META_LIST
        sample = random.sample(list, 1)[0]
        await ctx.send(str(sample))

    @commands.command(name='roll_pros_only', help='Rolls a random good Class that only Pros can play well.')
    async def roll_pros_only(self, ctx):
        list = OFF_META_LIST
        sample = random.sample(list, 1)[0]
        await ctx.send(str(sample))

    @commands.command(name='roll_solo', help='Rolls a random good Solo Class')
    async def roll_solo(self, ctx):
        list = META_SOLO_LIST
        sample = random.sample(list, 1)[0]
        await ctx.send(str(sample))

    @commands.command(name='roll_pro_solo_only', help='Rolls a random good Solo Class that only Pros can play well.')
    async def roll_pro_solo_only(self, ctx):
        list = OFF_META_SOLO_LIST
        sample = random.sample(list, 1)[0]
        await ctx.send(str(sample))


    @commands.command(name='slap', help='Slap someone with a random object')
    async def slap(self, ctx, target):
        sample = random.sample(SLAP_LIST, 1)[0]
        await ctx.send(sample.format(author = ctx.author, target = target))

