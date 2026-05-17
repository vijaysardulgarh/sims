// ============================================
// SANCTIONED POST FORM
// File: SanctionedPostForm.jsx
// ============================================

import {
  useEffect,
  useState
} from "react";

import postTypeService
from "../post-types/postTypeService";

const SanctionedPostForm = ({

  initialData = {},

  onSubmit,

  loading = false,

}) => {

  // ============================================
  // STATES
  // ============================================

  const [postTypes,
    setPostTypes] =
    useState([]);

  const [formData, setFormData] =
    useState({

      post_type: "",

      sanctioned_count: "",

      filled_count: "",

      remarks: "",
    });

  // ============================================
  // FETCH POST TYPES
  // ============================================

  useEffect(() => {

    fetchPostTypes();

  }, []);

  const fetchPostTypes = async () => {

    try {

      const response =
        await postTypeService.getPostTypes();

      setPostTypes(

        Array.isArray(response)

          ? response

          : response.results || []
      );

    } catch (error) {

      console.log(error);
    }
  };

  // ============================================
  // PREFILL
  // ============================================

  useEffect(() => {

    if (
      initialData &&
      Object.keys(initialData).length > 0
    ) {

      setFormData({

        post_type:
          initialData.post_type || "",

        sanctioned_count:
          initialData.sanctioned_count || "",

        filled_count:
          initialData.filled_count || "",

        remarks:
          initialData.remarks || "",
      });
    }

  }, [initialData]);

  // ============================================
  // HANDLE CHANGE
  // ============================================

  const handleChange = (e) => {

    const { name, value } = e.target;

    setFormData({

      ...formData,

      [name]: value,
    });
  };

  // ============================================
  // SUBMIT
  // ============================================

  const handleSubmit = (e) => {

    e.preventDefault();

    onSubmit(formData);
  };

  return (

    <form
      onSubmit={handleSubmit}
      className="
        bg-white
        rounded-2xl
        shadow
        p-6
        space-y-6
      "
    >

      {/* POST TYPE */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Post Type
        </label>

        <select

          name="post_type"

          value={formData.post_type}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "

          required
        >

          <option value="">
            Select Post Type
          </option>

          {

            postTypes.map((item) => (

              <option
                key={item.id}
                value={item.id}
              >

                {item.name}

              </option>
            ))
          }

        </select>

      </div>

      {/* SANCTIONED */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Sanctioned Count
        </label>

        <input

          type="number"

          name="sanctioned_count"

          value={formData.sanctioned_count}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "

          required
        />

      </div>

      {/* FILLED */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Filled Count
        </label>

        <input

          type="number"

          name="filled_count"

          value={formData.filled_count}

          onChange={handleChange}

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* REMARKS */}

      <div>

        <label className="
          block
          mb-2
          font-medium
        ">
          Remarks
        </label>

        <textarea

          name="remarks"

          value={formData.remarks}

          onChange={handleChange}

          rows="4"

          className="
            w-full
            border
            rounded-xl
            px-4
            py-3
          "
        />

      </div>

      {/* BUTTON */}

      <button

        type="submit"

        disabled={loading}

        className="
          bg-blue-600
          hover:bg-blue-700
          text-white
          px-6
          py-3
          rounded-xl
        "
      >

        {loading

          ? "Saving..."

          : "Save Sanctioned Post"}

      </button>

    </form>
  );
};

export default SanctionedPostForm;