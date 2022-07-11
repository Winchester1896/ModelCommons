<template>
    <div style="width:100%">
        <v-row>
            <v-col cols="3">
                  <v-select
                    v-model="selected_model"
                    :items="options_models"
                    item-text="text"
                    item-value="value"
                    label="Docker models"
                    return-object
                    single-line
                    ></v-select>
            
            </v-col>
            
            <v-col cols="5" >
                <v-textarea
                    label="docker run command"
                    auto-grow
                    v-model = "text_command"
                    outlined
                    rows="1"
                    row-height="15"
                ></v-textarea>
            </v-col>

            <v-col cols="4">
                <v-dialog
                v-model="dialog"
                persistent
                max-width="800px"
                >
                <template v-slot:activator="{ on, attrs }">
                <v-btn
                    color="primary"
                    v-bind="attrs"
                    v-on="on"
                >Add New Model</v-btn>
                </template>
                <v-card>
                    <v-toolbar
                        color="primary"
                        dark
                        >Add New Model</v-toolbar>
                        <v-card-text>
                        <v-container>
                            <v-row>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                                <v-text-field
                                label="Model Name*"
                                required
                                v-model="form_model_name"
                                ></v-text-field>
                            </v-col>
                            <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                                <v-text-field
                                label="Docker Run Command*"
                                v-model="form_model_command"
                                hint="the docker command with specified parameters."
                                ></v-text-field>
                            </v-col>
                            </v-row>
                        </v-container>
                        <small>*indicates required field</small>
                        </v-card-text>
                        <v-card-actions>
                        <v-spacer></v-spacer>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="dialog = false"
                        >
                            Close
                        </v-btn>
                        <v-btn
                            color="blue darken-1"
                            text
                            @click="submit"
                        >
                            Save
                        </v-btn>
                        </v-card-actions>
                </v-card>
            </v-dialog>
                
            </v-col>
        </v-row>
        <v-row>
            <v-col cols="3">
                 <v-select
                    v-model="selected_dataset"
                    :items="options_datasets"
                    item-text="text"
                    item-value="value"
                    label="Dataset"
                    persistent-hint
                    return-object
                    single-line
                    ></v-select>
            </v-col>
            <v-col cols="5">
                <v-textarea
                    label="future use"
                    auto-grow
                    outlined
                    rows="1"
                    row-height="15"
                ></v-textarea>
            </v-col>
            <v-col cols="auto">
                <v-dialog
                    persistent
                    max-width="600"
                >
                    <template v-slot:activator="{ on, attrs }">
                    <v-btn
                        color="primary"
                        v-bind="attrs"
                        v-on="on"
                    >Add New Dataset</v-btn>
                    </template>
                    <template v-slot:default="dialog">
                    <v-card>
                        <v-toolbar
                        color="primary"
                        dark
                        >Add New Dataset</v-toolbar>
                        <v-col
                                cols="12"
                                sm="6"
                                md="4"
                            >
                                <v-text-field
                                label="Dataset Name*"
                                required
                                v-model="form_dataset_name"
                                ></v-text-field>
                            </v-col>
                        <v-col
                            cols="12"
                            sm="6"
                            md="4"
                        >
                            <template>
                            <v-file-input
                                accept=".yml, .yaml"
                                label="File input*"
                            ></v-file-input>
                        </template>
                        <small>*indicates required field</small>
                        </v-col>
                        <v-card-actions class="justify-end">
                            <v-spacer></v-spacer>
                            <v-btn
                                color="blue darken-1"
                                text
                                @click="dialog.value = false"
                            >
                                Close
                            </v-btn>
                            <v-btn
                                color="blue darken-1"
                                text
                                @click="submit"
                            >
                                Upload
                            </v-btn>
                        </v-card-actions>
                    </v-card>
                    </template>
                </v-dialog>
            </v-col>

            <v-col cols="3">
                <v-btn depressed color="primary" @click="confirm">
                    Confirm
                </v-btn>
            </v-col>
        </v-row>
    </div>
</template>
<script>
export default {
    data(){
        return{
            selected_model: {},
            selected_dataset: {},
            options_datasets:[{
                text: "Soybean Leaf Defoliation",
                value: "leafdefo",
            },{
                text: "Add New",
                value: 'addnew'
            }],
            dialog: false, // show add new panel or not 
            // form to add new dataset
            form_model_name: "",
            form_model_command: "",
            text_command: "" // value for input of docker run command
        }
    },
    methods:{
        confirm(){
            if(this.text_command=="" || this.selected_dataset.value==undefined){
                alert('please select!')
            }
            var temp = {command: this.text_command, data: this.selected_dataset.value}
            
            this.$store.dispatch('submitModelData', temp)
        },
        async submit(){
            // add new model form submit
            this.dialog=false // hide the panel
            // send request 
            await this.$store.dispatch("addNewModel",{name: this.form_model_name, command: this.form_model_command})
            //  clear in put for next time 
            this.form_model_command = ''
            this.form_model_name = ''
            this.$store.dispatch('getModel')
        },
        updateOptionDataset(raw){
           
        }
    },
    created(){
        this.$store.dispatch('getModel')
    },
    watch:{
        selected_model(){
            let current = this.selected_model.value
            let command = this.dataset2Command[current]
            this.text_command = command
        }
    },
    computed:{
        dataset2Command(){
            return this.$store.state.dataset2Command
        },
        options_models(){
            console.log(this.dataset2Command)
            var temp = []
            for(let key in this.dataset2Command){ 
                temp.push({
                    text: key,
                    value: key
                })
            }
            return temp
        }
    }
}
</script>