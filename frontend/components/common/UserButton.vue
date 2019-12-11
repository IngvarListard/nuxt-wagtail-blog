<template>
  <v-menu
    open-on-hover
    bottom
    offset-y
    close-delay="300"
    transition="slide-y-reverse-transition"
  >
    <template #activator="{ on }">
      <v-avatar v-on="on">
        <v-img :src="formatAvatarUrl(user.avatar)" />
      </v-avatar>
    </template>
    <v-list>
      <list-item
        :btn="{
          name: 'Управление профилем',
          icon: 'mdi-settings-outline',
          route: `/profile/settings/general`
        }"
      />
<!--      <list-item-->
<!--        :btn="{-->
<!--          name: 'Закладки',-->
<!--          icon: 'mdi-bookmark-multiple-outline',-->
<!--          route: '/bookmarks-outline'-->
<!--        }"-->
<!--      />-->
      <list-item
        :btn="{
          name: 'Выход',
          icon: 'logout',
          route: '/logout'
        }"
      />
<!--      <list-item-->
<!--        :btn="{-->
<!--          icon: 'mdi-theme-light-dark'-->
<!--        }"-->
<!--      >-->
        <template #content>
          <v-switch exact />
        </template>
      </list-item>
    </v-list>
  </v-menu>
</template>

<script>
import { CURRENT_USER_CLIENT } from '../../graphql/users/queries'
import utilsMixin from '../../utils/utilsMixin'
import ListItem from './ListItem'

export default {
  name: 'UserButton',
  components: { ListItem },
  mixins: [utilsMixin],
  data() {
    return {
      user: {
        id: null,
        avatar: null
      }
    }
  },
  apollo: {
    user: {
      query: CURRENT_USER_CLIENT
    }
  }
}
</script>

<style scoped></style>
