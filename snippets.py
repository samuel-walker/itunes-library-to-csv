# Abandoned approaches

# Want to get rid of ugly or statements, but can't figure it out. Some appraoches
# included trying to iterate within an elif statement, but I couldn't figure it
# out!

# I'd prefer if I didn't have to crowd those or statements... How to do that?

for i in pl['Playlists']:
    if i['Name'] in lists:
        print('Ignore')
    elif for type in types in i:
        print('Ignore')
    else:
        print(i['Name'])

found = True

for i in pl['Playlists']:
    for type in types:
        if type in i:
            print('Ignore')
            found = True
            break
        else:
            found = False
        if found == True:
            break
        else:
            print(i['Name'])

for i in pl['Playlists']:
    for type in types:

# Pseudo-code

for each playlist:
    if the playlist contains an attribute in types:
        ignore it
    elif the playlist's name is in lists:
        ignore it
    else:
        keep it

# Using a hit variable

        if type in i:
            hit = True
        else:
            hit = False
        if hit == True:
            break
        elif hit == False:
            print(i['Name'])

    if i['Name'] in lists:
        print('Ignore')
    else:
        print(i['Name'])


# Using ElementTree

import xml.etree.ElementTree as ET
tree = ET.parse('Library.xml')
root = tree.getroot()

# one specific item attribute
print('Item #2 attribute:')
print(root[0][1].attrib)

# all item attributes
print('\nAll attributes:')
for elem in root:
    for subelem in elem:
        print(subelem.attrib)

# one specific item's data
print('\nItem #2 data:')
print(root[0][1].text)

# all items data
print('\nAll item data:')
for elem in root:
    for subelem in elem:
        print(subelem.text)

# Using untangle

def access():
    """
    Shows basic attribute access and node navigation.
    """
    o = untangle.parse(
        '<node id="5">This is cdata<subnode value="abc"/></node>'
    )
    return ("Node id = %s, subnode value = %s" %
            (o.node['id'], o.node.subnode['value']))


def siblings_list():
    """
    Shows child element iteration
    """
    o = untangle.parse('''
        <root>
            <child name="child1"/>
            <child name="child2"/>
            <child name="child3"/>
        </root>
        ''')
    return ','.join([child['name'] for child in o.root.child])


def access_cdata():
    """
    Shows how to handle CDATA elements
    """
    o = untangle.parse(
        '<node id="5">This is cdata<subnode value="abc"/></node>'
    )
    return ("%s" % (o.node.cdata))

import untangle
obj = untangle.parse('Library.xml')

for line in obj.plist.dict.array.dict:
    print(line)

for e in obj.plist.dict.array.dict:
    print(e)
