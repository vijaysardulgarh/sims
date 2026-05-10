import api from "./api";

const studentService = {

  // =========================================
  // GET ALL STUDENTS
  // =========================================

  getStudents: async () => {

    const response = await api.get(
      "/students/"
    );

    return response.data;
  },


  // =========================================
  // GET SINGLE STUDENT
  // =========================================

  getStudent: async (id) => {

    const response = await api.get(
      `/students/${id}/`
    );

    return response.data;
  },


  // =========================================
  // CREATE STUDENT
  // =========================================

  createStudent: async (data) => {

    const response = await api.post(
      "/students/",
      data
    );

    return response.data;
  },


  // =========================================
  // UPDATE STUDENT
  // =========================================

  updateStudent: async (
    id,
    data
  ) => {

    const response = await api.put(
      `/students/${id}/`,
      data
    );

    return response.data;
  },


  // =========================================
  // DELETE STUDENT
  // =========================================

  deleteStudent: async (id) => {

    const response = await api.delete(
      `/students/${id}/`
    );

    return response.data;
  },


  // =========================================
  // IMPORT STUDENTS
  // =========================================

  importStudents: async (file) => {

    try {

      const formData = new FormData();

      formData.append(
        "file",
        file
      );

      const response = await api.post(

        "/students/import/",

        formData,

        {
          headers: {
            "Content-Type":
              "multipart/form-data",
          },
        }
      );

      console.log(
        "IMPORT SUCCESS:",
        response.data
      );

      return response.data;

    } catch (error) {

      console.log(
        "IMPORT ERROR:",
        error
      );

      console.log(
        "ERROR RESPONSE:",
        error.response
      );

      throw error;
    }
  },


  // =========================================
  // EXPORT STUDENTS
  // =========================================

  exportStudents: () => {

    window.open(

      "http://127.0.0.1:8000/api/students/export/"
    );
  },

};

export default studentService;