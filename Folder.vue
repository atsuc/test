<template>
  <div class="folder">
    <span @click="toggleOpen" class="clickable">
      <span v-if="open">▼</span>
      <span v-else>▶︎</span>
    </span>
    <span @click="setClickedFolder(id)" :class="{'cliked-folder' : getClickedFolder == id}" class="clickable">
      <span v-if="open">□</span>
      <span v-else>■</span>
      {{ folder.name }}
    </span>
    <span  v-if="open">
      <folder v-for="(folder, index) in folder.children" :key=index :folder="folder" :parentId="id" :subId="String(index)">
      </folder>
    </span>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex"

export default {
  name: "Folder",
  props: {
    folder: Object,
    parentId: {
      type: String,
      default: ""
    },
    subId: {
      type: String,
      default: "0"
    }
  },
  data(){
    return{
      id: 0,
      open: true,
      clicked: false
    }
  },
  methods: {
    toggleOpen: function(){
      this.open = !this.open
    },
    toggleClicked: function(){
      this.clicked = !this.clicked
    },
    ...mapActions([
      'changeFolder'
    ]),
    setClickedFolder: function(id){
      this.changeFolder(id)
    }
  },
  computed: {
    ...mapGetters([
      'getClickedFolder'
    ])
  },
  created: function() {
    this.id = this.parentId + this.subId
  }
}
</script>

<style>
.folder{
  margin-left:20px;
}
.clickable{
  cursor: pointer;
}
.cliked-folder{
  background-color: aqua;
}
</style>
