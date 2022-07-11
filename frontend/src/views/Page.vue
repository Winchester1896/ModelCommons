<template>
  <div>
      <v-app>
    <v-app-bar
    app
      color="deep-purple accent-4"
      dark
      prominent
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
        
      <v-toolbar-title>Data Commons for Digital Agriculture</v-toolbar-title>

      <v-spacer></v-spacer>

      <v-btn icon>
        <v-icon>mdi-magnify</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-filter</v-icon>
      </v-btn>

      <v-btn icon>
        <v-icon>mdi-dots-vertical</v-icon>
      </v-btn>
    </v-app-bar>
    <v-navigation-drawer
      v-model="drawer"
      absolute
      bottom
      temporary app
    >

     <v-list>
        <v-list-item class="px-2">
        <v-list-item-avatar>
            <v-img src="../assets/xiaohua.jpg"></v-img>
        </v-list-item-avatar>
        </v-list-item>

        <v-list-item link>
        <v-list-item-content>
            <v-list-item-title class="text-h6">
            Zichen Zhang
            </v-list-item-title>
            <v-list-item-subtitle>zhang.9325@osu.edu</v-list-item-subtitle>
        </v-list-item-content>
        </v-list-item>
    </v-list>
    <v-divider></v-divider>
    <v-list
        nav
        dense
    >
        <v-list-item link>
        <v-list-item-icon>
            <v-icon>mdi-folder</v-icon>
        </v-list-item-icon>
        <v-list-item-title>My Files</v-list-item-title>
        </v-list-item>
        <v-list-item link>
        <v-list-item-icon>
            <v-icon>mdi-account-multiple</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Shared with me</v-list-item-title>
        </v-list-item>
        <v-list-item link>
        <v-list-item-icon>
            <v-icon>mdi-star</v-icon>
        </v-list-item-icon>
        <v-list-item-title>Starred</v-list-item-title>
        </v-list-item>
    </v-list>

    <template v-slot:append>
        <div class="pa-2">
          <v-btn block>
            Logout
          </v-btn>
        </div>
      </template>
    </v-navigation-drawer>
      
      <v-main>
          <v-container fluid>
              <transition name="slide-fade" mode = "out-in">
                    <keep-alive>
                        <router-view></router-view>
                    </keep-alive>
                </transition>
          </v-container>
      </v-main>
      <v-footer app></v-footer>
      </v-app>
   
    

        
   
  </div>
</template>
<script>
  export default {
    data: () => ({
      drawer: false,
      group: null,
    }),

    watch: {
      group () {
        this.drawer = false
      },
    },
  }
</script>

<style>

</style>