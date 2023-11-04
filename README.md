# swat-discord-bot
Discord community bot for the Warcraft III custom game, SWAT: Aftermath

Requirements:
1. pip
2. discord.py
3. tabulate
4. python-dotenv

Alias commands:
```
alias restart-bot="kill \$(ps aux | grep '[s]watcc' | awk '{print \$2}') && python3 ~/swat-discord-bot/swatcc.py </dev/null &>/dev/null &"
alias start-bot="python3 ~/swat-discord-bot/swatcc.py </dev/null &>/dev/null &"
alias start-bot-debug="python3 ~/swat-discord-bot/swatcc.py"
alias stop-bot="kill \$(ps aux | grep '[s]watcc' | awk '{print \$2}')"
alias deploy-bot="stop-bot && git fetch && git reset --hard origin/master && start-bot"
```
