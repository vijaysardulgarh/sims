export default function ModuleForm({

    formData,

    handleChange,

    handleSubmit,

    isEdit,
}) {

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-6"
        >

            {/* NAME */}

            <div>

                <label className="block mb-2 font-medium">

                    Module Name

                </label>

                <input
                    type="text"
                    name="name"
                    value={formData.name}
                    onChange={handleChange}
                    placeholder="Enter module name"
                    required
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        px-4
                        py-3
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                />

            </div>


            {/* SLUG */}

            <div>

                <label className="block mb-2 font-medium">

                    Slug

                </label>

                <input
                    type="text"
                    name="slug"
                    value={formData.slug}
                    onChange={handleChange}
                    placeholder="Enter module slug"
                    required
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        px-4
                        py-3
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                />

            </div>


            {/* DESCRIPTION */}

            <div>

                <label className="block mb-2 font-medium">

                    Description

                </label>

                <textarea
                    name="description"
                    value={formData.description}
                    onChange={handleChange}
                    placeholder="Enter description"
                    rows="4"
                    className="
                        w-full
                        border
                        border-gray-300
                        rounded-xl
                        px-4
                        py-3
                        focus:outline-none
                        focus:ring-2
                        focus:ring-blue-500
                    "
                />

            </div>


            {/* ACTIVE */}

            <div className="flex items-center gap-3">

                <input
                    type="checkbox"
                    name="is_active"
                    checked={formData.is_active}
                    onChange={handleChange}
                />

                <label>

                    Is Active

                </label>

            </div>


            {/* BUTTON */}

            <button
                type="submit"
                className="
                    bg-blue-600
                    hover:bg-blue-700
                    text-white
                    px-6
                    py-3
                    rounded-xl
                    transition
                "
            >

                {isEdit
                    ? "Update Module"
                    : "Create Module"}

            </button>

        </form>
    );
}