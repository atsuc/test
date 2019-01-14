import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
    state: {
        title: 'My custom title',
        links: [
            'http://google.com',
            'http://aaa.com',
            'http://bbb.com'
        ],
        clikedFolder: ''
    },
    getters: {
        countLinks: state => {
            return state.links.length
        },
        getClickedFolder: state =>  {
            return state.clikedFolder
        }
    },
    mutations: {
        ADD_LINK: (state, link) => {
            state.links.push(link)
        },
        REMOVE_LINK: (state, link) => {
            state.links.splice(link, 1)
        },
        REMOVE_ALL: (state) => {
            state.links = []
        },
        CHANGE_FOLDER: (state, folder) => {
            state.clikedFolder = folder
        }
    },
    actions: {
        removeLink: (context, link) => {
            context.commit("REMOVE_LINK", link)
        },
        removeAll({commit}) {
            return new Promise((resolve, reject) => {
                setTimeout(() => {
                    commit('REMOVE_ALL')
                    resolve()
                }, 1500)
            })
        },
        changeFolder: (context, folder) => {
            context.commit("CHANGE_FOLDER", folder)
        }
    }
})
