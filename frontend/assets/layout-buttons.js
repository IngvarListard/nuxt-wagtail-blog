export const buttons = [
  {
    name: 'Главная',
    icon: 'home',
    route: '/'
  },
  {
    name: 'Категории',
    icon: 'mdi-shape',
    route: '/categories',
    categories: [
      {
        name: 'Django',
        route: '/categories/django'
      },
      {
        name: 'Vue',
        route: '/categories/vue'
      },
      {
        name: 'Apollo',
        route: '/categories/apollo'
      }
    ]
  },
  {
    name: 'Рекомендации',
    icon: 'mdi-thumb-up',
    route: '/recommendations',
    categories: [
      {
        name: 'Лучший дистрибутив',
        route: '/'
      },
      {
        name: 'Софт',
        route: '/'
      },
      {
        name: 'Хард',
        route: '/'
      }
    ]
  }
]

