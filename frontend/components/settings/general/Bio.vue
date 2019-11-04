<template>
  <settings-card :title-class="['my-1', 'py-1']">
    <template #title>
      <v-row align="center" dense class="my-0 py-0">
        <div>Коротко о себе</div>
        <v-spacer />
        <v-list-item-action>
          <v-btn icon>
            <v-icon>mdi-pencil</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-row>
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
