from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response



# Create your views here.


class StudentView(APIView):
    def get(self, request, *args, **kwargs):
        queryset = Student.objects.all()
        serializer = StudentSerializer(queryset, many=True)
        return Response(serializer.data)
    def delete(self, request, *args, **kwargs):
        try:
            student = Student.objects.get(pk=kwargs.get('pk'))
            student.delete()
            queryset = Student.objects.all()
            serializer = StudentSerializer(queryset, many=True)
            return Response({
                'detail' : 'Student Deleted Successfully!',
                'data' : serializer.data,
            })
        except Student.DoesNotExist:
            return Response({'detail' : 'Student not Deleted!'})
    def post(self, request, *args, **kwargs):
        student = StudentSerializer(data=request.data)
        if student.is_valid():
            student.save()
            return Response({'detail' : 'Student Added'})
        else:
            return Response({'detail' : 'Student not Added'})
    # def put(self, pk, response, *args, **kwargs):
    #     # student = Student.objects.get(pk=request.data.id)
    #     # newStudent = StudentSerializer(student, data=request.data)
    #     # if newStudent.is_valid():
    #     #     newStudent.save()
    #     # return Response({'details' : 'Student Updated Successfully!'})
    #     try:
    #         student = self.get_object(pk)
    #         new_student_data = request.data  # Rename to new_student_data for clarity
    #         new_student_serializer = StudentSerializer(student, data=new_student_data)

    #         if new_student_serializer.is_valid():
    #             new_student_serializer.save()
    #             return Response({'details': 'Student Updated Successfully!'})
            
    #         return Response(new_student_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    #     except Student.DoesNotExist:
    #         return Response({'details': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        
    #     except Exception as e:
    #         return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student, data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response({'details': 'Student Updated Successfully!'})

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Student.DoesNotExist:
            return Response({'details': 'Student not found'}, status=status.HTTP_404_NOT_FOUND)
        