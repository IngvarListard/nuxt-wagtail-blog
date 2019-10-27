<template>
  <settings-card>
    <template #title>
      Коротко о себе
    </template>
    <template #body>
      <v-card-text>
        <div class="text-primary">
          Lorem ipsum dolor sit amet, consectetur adipisicing elit. Aliquam aut
          culpa deleniti ea esse impedit, necessitatibus nobis, officiis
          repellat reprehenderit veniam, voluptates. Aperiam debitis dolorum
          eaque earum est officiis sapiente. Lorem ipsum dolor sit amet,
          consectetur adipisicing elit. Ad, aliquid commodi culpa debitis
          deserunt error facere fuga hic iste maiores necessitatibus, nostrum
          perferendis quaerat quo repellat sint tempore, voluptas voluptatibus?
        </div>
      </v-card-text>
    </template>
  </settings-card>
</template>

<script>
import SettingsCard from './SettingsCard'
export default {
  name: 'Bio',
  components: { SettingsCard }
}
</script>

<style scoped></style>
