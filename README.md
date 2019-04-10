# bpConvert
Simple script/class to convert between entities within Factorio blueprints using python3

1) Clone repo
2) copy the blueprint string you want to convert into a file
3) run `python main.py {{ file-name }} {{ old-entity-name }} {{ new-entity-name }}`
4) Find internal entity names at Factorio Wiki (i.e. https://wiki.factorio.com/Express_transport_belt and look for 'Internal Name' on the right)

i.e. `python main.py exampleInput.txt fast-transporter-belt express-transporter-belt`

5) Output will be the new blueprint string, which you can import into your Factorio blueprint library in-game

