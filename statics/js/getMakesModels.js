const app = new Vue({
    // Django template use "{{ value }}"
    delimiters: ['[[', ']]'],
    el: '#app',
    data: {
        allData: new Array(),
        makeSelected: '',
        modelSelected: '',
        models: [],
        allMakesKeys: [],
    },
    methods: {
        async getMakes() {
            let makes = await axios.get(
                'http://localhost:5000/api/makes'
            );
            this.allData = makes.data
            this.makeSelected = this.allData[0].key
        },
        async getModels(key) {
            let allModels = await axios.get(
                'http://localhost:5000/api/makes', {
                    params: {
                        keymake: key
                    }
                } 
            );
            //console.log("Test")
            console.log(allModels)
            this.models = allModels.data[0];
            //console.log(this.models)
        },
        onChangeSelecte () {
            this.getModels(this.makeSelected);
        }
    },
    mounted() {
        this.getMakes()
    },
    created(){
        this.getModels(this.makeSelected)
    }
})