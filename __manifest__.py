{
    'name': 'OWL Todo',
    'version': '1.0',
    'summary': 'OWL Todo app for practicing OWL JS',
    'sequence': -1,
    'description': """Developed by MD. Ashikuzzaman.""",
    'category': '',
    'website': '',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/views_menu.xml'
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'assets': {
        'web.assets_backend': [
            'owl_todo/static/src/components/todo_list/todo_list.js',
            'owl_todo/static/src/components/todo_list/todo_list.xml',
            'owl_todo/static/src/components/todo_list/todo_list.css'
        ]
    },
    'license': 'LGPL-3',
}
