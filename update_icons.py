from urllib.request import urlopen
import re

WEBFONT_VARIABLES_SCSS_URL = 'https://raw.githubusercontent.com/Templarian/MaterialDesign-Webfont/master/scss/_variables.scss'


def main():
    scss_string: str = urlopen(
        WEBFONT_VARIABLES_SCSS_URL).read().decode('utf-8')
    # some extra cool parsing
    search1_str = '$mdi-icons: ('
    index_1 = scss_string.find(search1_str) + len(search1_str)
    index_2 = scss_string.find(');', index_1 + 1)

    icons_map = scss_string[index_1:index_2].strip()
    # some fixing scss -> js
    icons_map = re.sub('^ *"(.+?)": (.+?),? *$',
                       '    "\\1": "\\2",', icons_map, flags=re.M)
    out = f"""
const mdiIcons = {{
{icons_map}
}}"""
    with open('icons.js', 'w') as f:
        f.write(out)


if __name__ == '__main__':
    main()
