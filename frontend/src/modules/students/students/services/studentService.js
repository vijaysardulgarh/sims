import api from "../../../../services/api/axios";


const studentService = {

  // =========================================
  // GET ALL STUDENTS
  // =========================================

  getStudents: async (
    params = {}
  ) => {

    const response = await api.get(

      "/students/",

      {
        params
      }
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

  createStudent: async (
    data
  ) => {

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

    const response = await api.patch(

      `/students/${id}/`,

      data
    );

    return response.data;
  },


  // =========================================
  // DELETE STUDENT
  // =========================================

  deleteStudent: async (
    id
  ) => {

    const response = await api.delete(

      `/students/${id}/`
    );

    return response.data;
  },


  // =========================================
  // BULK DELETE STUDENTS
  // =========================================

  bulkDeleteStudents: async (
    ids
  ) => {

    const response = await api.post(

      "/students/bulk-delete/",

      {
        ids
      }
    );

    return response.data;
  },


  // =========================================
  // SEARCH STUDENTS
  // =========================================

  searchStudents: async (
    query
  ) => {

    const response = await api.get(

      "/students/",

      {
        params: {
          search: query
        }
      }
    );

    return response.data;
  },


  // =========================================
  // IMPORT STUDENTS
  // =========================================

  importStudents: async (
    file
  ) => {

    try {

      const formData =
        new FormData();

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

      `${api.defaults.baseURL}/students/export/`
    );
  },

};


export default studentService;