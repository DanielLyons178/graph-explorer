from . import Plugin


class CatchallDiamondPlugin(Plugin):
    """
    Like catchall, but for targets from diamond (presumably)
    """
    priority = -4

    targets = [
        {
            'match': '^servers\.(?P<server>[^\.]+)\.(?P<tosplit>.*)',
            'target_type': 'unknown',
            'tags': {
                'unit': 'unknown',
                'source': 'diamond'
            },
            'configure': lambda self, target: self.autosplit(target)
        },
    ]


# vim: ts=4 et sw=4:
