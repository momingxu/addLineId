#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# target script

import sys
from lxml import etree

XHTML_NAMESPACE = 'http://www.w3.org/1999/xhtml'

def run(bk):
    for mid, href in bk.text_iter():
        print("..converting: ", href, " with manifest id: ", mid)
        bk.writefile(mid,add_line_id(bk.readfile(mid)))
    return 0


def add_line_id(content):
    parser = etree.XMLParser(resolve_entities=False, encoding='utf-8')
    root = etree.fromstring(content.encode('utf-8'), parser=parser)
    body = root.xpath('//xhtml:p | //xhtml:img |//xhtml:h1 | //xhtml:h2 | //xhtml:h3 | //xhtml:h4 | //xhtml:h5 | //xhtml:h6', namespaces={'xhtml': XHTML_NAMESPACE})

    for i, p in enumerate(body):
        try:
            p.attrib['id']
        except:
            p.attrib['id'] = 'kobo.%s' % i
    return etree.tostring(root, encoding='utf-8')

    


def main():
    print('11111111')
    return -1

if __name__ == "__main__":
    sys.exit(main())
