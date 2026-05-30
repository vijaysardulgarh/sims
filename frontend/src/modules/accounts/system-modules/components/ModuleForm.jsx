export default function ModuleForm({

    formData,

    handleChange,

    handleSubmit,

    isEdit,

    parentModules = [],
}) {

    return (

        <form
            onSubmit={handleSubmit}
            className="space-y-6"
        >

            {/* PARENT MODULE */}

            <div>

                <label className="block mb-2 font-medium">

                    Parent Module

                </label>

                <select
                    name="parent"
                    value={formData.parent || ""}
                    onChange={handleChange}
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
                >

                    <option value="">

                        Main Module

                    </option>

                    {
                        parentModules.map((module) => (

                            <option
                                key={module.id}
                                value={module.id}
                            >

                                {module.name}

                            </option>
                        ))
                    }

                </select>

            </div>


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


            {/* PATH */}

            <div>

                <label className="block mb-2 font-medium">

                    Frontend Path

                </label>

                <input
                    type="text"
                    name="path"
                    value={formData.path || ""}
                    onChange={handleChange}
                    placeholder="/dashboard/users"
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


            {/* ICON */}

            <div>

                <label className="block mb-2 font-medium">

                    Icon

                </label>

                <input
                    type="text"
                    name="icon"
                    value={formData.icon || ""}
                    onChange={handleChange}
                    placeholder="Users"
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


            {/* ORDER */}

            <div>

                <label className="block mb-2 font-medium">

                    Menu Order

                </label>

                <input
                    type="number"
                    name="order"
                    value={formData.order || 0}
                    onChange={handleChange}
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


            {/* IS MENU */}

            <div className="flex items-center gap-3">

                <input
                    type="checkbox"
                    name="is_menu"
                    checked={formData.is_menu}
                    onChange={handleChange}
                />

                <label>

                    Show In Sidebar

                </label>

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