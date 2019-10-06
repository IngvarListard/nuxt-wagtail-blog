export const state = () => ({
  notifications: []
})

// TODO: если видимых уведомлений больше например 5, то просто скрывать их когда появляются новые
export const mutations = {
  addNotification({ notifications }, notification) {
    notification = Object.assign({ show: true, displayed: false }, notification)
    const displayedNotifications = notifications.filter(n => n.show)
    if (displayedNotifications.length >= 5) {
      displayedNotifications.forEach((n, i) => {
        if (i > 3) n.show = false
      })
    }
    notifications.unshift(notification)
  },
  shiftNotification() {},
  setDisplayStatus({ notifications }, { id, show, displayed }) {
    const notification = notifications.find(n => n.id === id)
    if (notification) {
      notification.show = show
      notification.displayed = displayed
    }
  }
}

export const actions = {
  addPopup(ctx, notification) {
    ctx.commit('addNotification', notification)
    // время отображения
    setTimeout(() => {
      ctx.commit('setDisplayStatus', { id: notification.id, show: false })
    }, 8000)
    // при исчезновении из списка в уведомлениях не срабатывает
    // анимация, поэтому помечаем как "displayed" после отрисовки анимации
    setTimeout(() => {
      ctx.commit('setDisplayStatus', {
        id: notification.id,
        show: false,
        displayed: true
      })
    }, 9000)
  }
}

export const getters = {
  nonDisplayedNotifications({ notifications }) {
    return notifications
      .filter(n => !n.displayed)
      .slice()
      .reverse()
  }
}
