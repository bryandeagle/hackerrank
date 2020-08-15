def get_attr_number(node):
    if not node:
        # print('NODE={},SCORE={}'.format(node.tag, len(node.attrib)))
        return len(node.attrib)
    else:
        x = len(node.attrib)
        for child in node:
            x += get_attr_number(child)
        # print('NODE={},SCORE={}'.format(node.tag, x))
        return x
