<template>
  <div>
    <div class="display-3 mb-3">Случайная статья</div>
    <random-article />
    <portal to="bottom">
      <feed />
    </portal>
  </div>
</template>

<script>
import RandomArticle from '../components/blog/RandomArticle'
import Feed from '../components/blog/Feed'

export default {
  components: { RandomArticle, Feed }
}
</script>
