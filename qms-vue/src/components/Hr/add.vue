<template>
  <v-form ref="form" v-model="valid" lazy-validation>

    <v-text-field v-model="hrd" :counter="100" :rules="hrdRules" label="HR Required for Designation" required></v-text-field>
    <v-text-field v-model="reason" :counter="400" :rules="reasonRules" label="Reason for New Hiring" required></v-text-field>
    <v-text-field v-model="requiested" :counter="50" :rules="requiestedRules" label="Requested By" required></v-text-field>
    <v-text-field v-model="remark" :counter="400"  label="Remarks" required></v-text-field>

    <v-btn :disabled="!valid" color="success" @click="validate" > Submit </v-btn>
    <v-btn color="error" @click="reset">Reset Form</v-btn>
    <v-btn color="warning" @click.stop="drawer = !drawer" >Cancel</v-btn>

  </v-form>
</template>

<script>

export default {
  data: () => ({
    drawer: null,
    valid: true,
    
    hrd: "",
    reason: "",
    requiested: "",
    remark:"",
    
    hrdRules: [
      v => !!v || "HR Required for Designation is required",
      v => (v && v.length <= 100) || "HR Required for Designation must be less than 100 characters"
    ],
    reasonRules: [
      v => !!v || "Reason for New Hiring is required",
      v => (v && v.length <= 400) || "Reason for New Hiring must be less than 100 characters"
    ],
    requiestedRules: [
      v => !!v || "Requested By is required",
      v => (v && v.length <= 50) || "Requested By must be less than 100 characters"
    ],
  }),

  methods: {
    validate() {
      if (this.$refs.form.validate()) {
        this.snackbar = true;
        
        axios.post('http://localhost:8000/api/v1/hr/', {
            hr_required_deg: this.hrd,
            requestedby: this.reason,
            reson_new_hire: this.reason,
            remarks: this.remark,
            preparedBy:'sdf',
            arrovedBy:'sd',
        })
        .then(function (response) {
            console.log(response);
            router.push("/dashboard");
        })
        .catch(function (error) {
            console.log(error);
        });
      }
    },
    reset() {
      this.$refs.form.reset();
    },
    resetValidation() {
      this.$refs.form.resetValidation();
    }
  }
};
</script>