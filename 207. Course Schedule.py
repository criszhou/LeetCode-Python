class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courseToPrereq = { course : set() for course in range(numCourses) }
        prereqToCourse = { course : set() for course in range(numCourses) }
        for course,prereq in prerequisites:
            courseToPrereq[course].add(prereq)
            prereqToCourse[prereq].add(course)

        numCoursesTaken = 0

        nextCandidates = { course for course in range(numCourses) if not courseToPrereq[course] }
        while nextCandidates:

            currCourse = nextCandidates.pop()
            # assert not courseToPrereq[currCourse]
            numCoursesTaken += 1

            for futureCourse in prereqToCourse[currCourse]:
                courseToPrereq[futureCourse].remove(currCourse)
                if not courseToPrereq[futureCourse]:
                    nextCandidates.add( futureCourse )

            del prereqToCourse[ currCourse ]
            del courseToPrereq[ currCourse ]

        return numCoursesTaken == numCourses